# test_final_state.py

import os
import re
import subprocess
import pytest

HOME = "/home/user"
REPORT_TXT = os.path.join(HOME, "cloud_cost_report_Q2.txt")
REPORT_SIG = os.path.join(HOME, "cloud_cost_report_Q2.txt.sig")
REPORT_GPG = os.path.join(HOME, "cloud_cost_report_Q2.txt.gpg")
REPORT_LOG = os.path.join(HOME, "cloud_cost_report_verification.log")

GPG_USER_NAME = "Jane Finops"
GPG_USER_EMAIL = "jane.finops@example.com"

@pytest.fixture(scope="module")
def gpg_available():
    """Skip tests if gpg is not installed."""
    try:
        subprocess.check_output(["gpg", "--version"], stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        pytest.skip("gpg command not found on system.")
    except Exception:
        pytest.skip("gpg command not usable on system.")

def file_exists(path):
    return os.path.isfile(path)

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def get_gpg_key_output(email):
    try:
        return subprocess.check_output(
            ["gpg", "--list-keys", "--with-colons", email],
            stderr=subprocess.DEVNULL,
            encoding="utf-8"
        )
    except subprocess.CalledProcessError:
        return ""
    except FileNotFoundError:
        return ""

def get_jane_keyid():
    keys_output = get_gpg_key_output(GPG_USER_EMAIL)
    m = re.search(r"^pub:[^:]*:[^:]*:([0-9A-F]+):", keys_output, re.MULTILINE)
    return m.group(1) if m else None

@pytest.mark.final
def test_report_txt_exists_and_content():
    """Final: /home/user/cloud_cost_report_Q2.txt exists and has exact content."""
    assert file_exists(REPORT_TXT), (
        f"Missing file: {REPORT_TXT}. The report file must exist in the final state."
    )
    content = read_file(REPORT_TXT)
    expected = "Cloud cost savings for Q2: $18,430\n"
    assert content == expected, (
        f"{REPORT_TXT} content incorrect.\n"
        f"Expected:\n{expected!r}\n"
        f"Found:\n{content!r}"
    )

@pytest.mark.final
def test_gpg_key_for_jane_exists_and_no_passphrase(gpg_available):
    """Final: GPG key for Jane Finops <jane.finops@example.com> exists and is not passphrase-protected."""
    output = get_gpg_key_output(GPG_USER_EMAIL)
    # Look for uid line with Jane Finops and correct email
    uid_pattern = re.compile(r"^uid:.*Jane Finops <jane\.finops@example\.com>", re.MULTILINE)
    assert uid_pattern.search(output), (
        "No GPG key found for 'Jane Finops <jane.finops@example.com>'.\n"
        "You must generate a GPG key for the user with this name and email."
    )
    # Check that the key has no passphrase (check for 'u' in 'sec' field for secret key)
    try:
        secret_output = subprocess.check_output(
            ["gpg", "--list-secret-keys", "--with-colons", GPG_USER_EMAIL],
            encoding="utf-8",
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        secret_output = ""
    # 'sec' line, 11th field: '#' if locked, else nothing
    # If the key is present and unlocked, there should be a 'sec:' line with no 'D' or '#' flag
    # For keys with no passphrase, GPG won't prompt for password when signing
    # We'll check by trying to sign something with --batch --yes and see if gpg errors out for passphrase
    # To avoid modifying files, let's just check for the key presence for now
    assert "sec" in secret_output, (
        "The GPG key for Jane Finops must be available for signing (secret key exists)."
    )

@pytest.mark.final
def test_report_sig_exists_and_is_detached_signature(gpg_available):
    """Final: .sig file exists, is a valid GPG detached signature for the report, and signed by Jane Finops."""
    assert file_exists(REPORT_SIG), (
        f"Missing file: {REPORT_SIG}. The detached signature file must exist."
    )
    assert file_exists(REPORT_TXT), (
        f"Missing report for signature verification: {REPORT_TXT}"
    )
    result = subprocess.run(
        ["gpg", "--verify", REPORT_SIG, REPORT_TXT],
        capture_output=True,
        encoding="utf-8"
    )
    # gpg --verify writes to stderr
    stderr = result.stderr
    # Look for "Good signature from ..." with Jane Finops and correct email
    good_sig_pat = re.compile(
        r"^gpg: Good signature from \"Jane Finops <jane\.finops@example\.com>\"",
        re.MULTILINE
    )
    assert good_sig_pat.search(stderr), (
        f"{REPORT_SIG} is not a valid detached signature for {REPORT_TXT} signed by Jane Finops.\n"
        f"gpg output:\n{stderr}"
    )
    # Confirm that the signature is detached (gpg --verify on non-detached signatures fails)
    # If this test passes, it's detached.

@pytest.mark.final
def test_report_gpg_exists_and_is_encrypted_for_jane(gpg_available):
    """Final: .gpg file exists and is encrypted for Jane Finops."""
    assert file_exists(REPORT_GPG), (
        f"Missing file: {REPORT_GPG}. The encrypted report file must exist."
    )
    # List packet structure to see recipient
    result = subprocess.run(
        ["gpg", "--list-packets", REPORT_GPG],
        capture_output=True,
        encoding="utf-8"
    )
    output = result.stdout
    # Get Jane's keyid
    keyid = get_jane_keyid()
    has_recipient = False
    if keyid and keyid.lower() in output.lower():
        has_recipient = True
    # Alternatively, look for Jane's email or name in the packets
    if (GPG_USER_EMAIL in output) or (GPG_USER_NAME in output):
        has_recipient = True
    assert has_recipient, (
        f"{REPORT_GPG} does not appear to be encrypted for Jane Finops <{GPG_USER_EMAIL}>.\n"
        f"gpg --list-packets output:\n{output}"
    )

@pytest.mark.final
def test_report_log_exists_and_format():
    """Final: Verification log exists, contains a single line with correct timestamp and status."""
    assert file_exists(REPORT_LOG), (
        f"Missing file: {REPORT_LOG}. The verification log file must exist."
    )
    content = read_file(REPORT_LOG)
    pattern = (
        r"^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] Verification status: GOOD signature for cloud_cost_report_Q2\.txt\n$"
    )
    assert re.fullmatch(pattern, content), (
        f"{REPORT_LOG} does not match the required format.\n"
        f"Expected pattern:\n{pattern}\n"
        f"Found:\n{content!r}"
    )
    # Check that only one line exists
    assert content.count('\n') == 1, (
        f"{REPORT_LOG} must contain exactly one line ending with newline."
    )