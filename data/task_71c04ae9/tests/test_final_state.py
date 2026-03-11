# test_final_state.py

import os
import pytest

DEPLOYMENTS_DIR = "/home/user/deployments"
AUDIT_LOG = "/home/user/rotation_audit.log"
OLD_KEY = "sk-OLDKEY-v1-abc123def456"
NEW_KEY = "sk-NEWKEY-v2-xyz789uvw012"

# Files that should have been modified (old key replaced with new key)
MODIFIED_FILES = {
    "/home/user/deployments/app/service.conf": (
        "[service]\n"
        "name=payment-api\n"
        "api_key=sk-NEWKEY-v2-xyz789uvw012\n"
        "timeout=30\n"
    ),
    "/home/user/deployments/db/primary.conf": (
        "[database]\n"
        "host=db.internal\n"
        "port=5432\n"
        "api_key=sk-NEWKEY-v2-xyz789uvw012\n"
        "pool_size=10\n"
    ),
    "/home/user/deployments/gateway/proxy.conf": (
        "[proxy]\n"
        "upstream=backend:8080\n"
        "api_key=sk-NEWKEY-v2-xyz789uvw012\n"
        "tls=true\n"
        "retries=3\n"
    ),
}

# Files that should remain untouched
UNMODIFIED_FILES = {
    "/home/user/deployments/app/worker.conf": (
        "[worker]\n"
        "name=background-worker\n"
        "max_retries=5\n"
        "log_level=info\n"
    ),
    "/home/user/deployments/db/replica.conf": (
        "[database]\n"
        "host=replica.internal\n"
        "port=5432\n"
        "pool_size=5\n"
        "readonly=true\n"
    ),
    "/home/user/deployments/gateway/tls.conf": (
        "[tls]\n"
        "cert=/etc/ssl/certs/service.crt\n"
        "key=/etc/ssl/private/service.key\n"
        "protocols=TLSv1.2,TLSv1.3\n"
    ),
}

EXPECTED_AUDIT_CONTENT = (
    "/home/user/deployments/app/service.conf\n"
    "/home/user/deployments/db/primary.conf\n"
    "/home/user/deployments/gateway/proxy.conf\n"
)


# ── Directory structure ──────────────────────────────────────────────────────

def test_deployments_directory_exists():
    assert os.path.isdir(DEPLOYMENTS_DIR), (
        f"Deployments directory does not exist: {DEPLOYMENTS_DIR}"
    )


def test_subdirectories_exist():
    for subdir in ["app", "db", "gateway"]:
        path = os.path.join(DEPLOYMENTS_DIR, subdir)
        assert os.path.isdir(path), (
            f"Expected subdirectory does not exist: {path}"
        )


# ── Modified files contain new key and correct content ───────────────────────

@pytest.mark.parametrize("filepath,expected_content", list(MODIFIED_FILES.items()))
def test_modified_file_has_new_key_content(filepath, expected_content):
    assert os.path.isfile(filepath), (
        f"Expected .conf file does not exist: {filepath}"
    )
    with open(filepath, "r") as f:
        actual = f.read()
    assert actual == expected_content, (
        f"File {filepath} does not have the expected final content.\n"
        f"Expected:\n{expected_content!r}\n"
        f"Actual:\n{actual!r}"
    )


@pytest.mark.parametrize("filepath", sorted(MODIFIED_FILES.keys()))
def test_modified_file_does_not_contain_old_key(filepath):
    assert os.path.isfile(filepath), (
        f"File does not exist: {filepath}"
    )
    with open(filepath, "r") as f:
        content = f.read()
    assert OLD_KEY not in content, (
        f"File {filepath} still contains the old API key '{OLD_KEY}'.\n"
        f"The key replacement was not performed correctly.\n"
        f"Actual content:\n{content!r}"
    )


@pytest.mark.parametrize("filepath", sorted(MODIFIED_FILES.keys()))
def test_modified_file_contains_new_key(filepath):
    assert os.path.isfile(filepath), (
        f"File does not exist: {filepath}"
    )
    with open(filepath, "r") as f:
        content = f.read()
    assert NEW_KEY in content, (
        f"File {filepath} does not contain the new API key '{NEW_KEY}'.\n"
        f"Actual content:\n{content!r}"
    )


# ── Unmodified files are byte-for-byte identical to originals ────────────────

@pytest.mark.parametrize("filepath,expected_content", list(UNMODIFIED_FILES.items()))
def test_unmodified_file_is_unchanged(filepath, expected_content):
    assert os.path.isfile(filepath), (
        f"Expected .conf file does not exist: {filepath}"
    )
    with open(filepath, "r") as f:
        actual = f.read()
    assert actual == expected_content, (
        f"File {filepath} was supposed to remain untouched but its content changed.\n"
        f"Expected (original):\n{expected_content!r}\n"
        f"Actual:\n{actual!r}"
    )


@pytest.mark.parametrize("filepath", sorted(UNMODIFIED_FILES.keys()))
def test_unmodified_file_does_not_contain_old_key(filepath):
    """These files never had the old key; confirm they still don't."""
    with open(filepath, "r") as f:
        content = f.read()
    assert OLD_KEY not in content, (
        f"File {filepath} should never have contained '{OLD_KEY}', but now it does.\n"
        f"Actual content:\n{content!r}"
    )


@pytest.mark.parametrize("filepath", sorted(UNMODIFIED_FILES.keys()))
def test_unmodified_file_does_not_contain_new_key(filepath):
    """These files never had the old key; the new key should not have been injected."""
    with open(filepath, "r") as f:
        content = f.read()
    assert NEW_KEY not in content, (
        f"File {filepath} should not contain the new key '{NEW_KEY}', but it does.\n"
        f"It appears the replacement was applied to files that should not have been touched.\n"
        f"Actual content:\n{content!r}"
    )


# ── No unexpected .conf files ────────────────────────────────────────────────

def test_no_extra_conf_files():
    """Ensure there are no unexpected .conf files in the deployments directory."""
    found_conf_files = set()
    for root, dirs, files in os.walk(DEPLOYMENTS_DIR):
        for fname in files:
            if fname.endswith(".conf"):
                found_conf_files.add(os.path.join(root, fname))

    all_expected = set(MODIFIED_FILES.keys()) | set(UNMODIFIED_FILES.keys())
    extra = found_conf_files - all_expected
    assert not extra, (
        f"Found unexpected .conf files in {DEPLOYMENTS_DIR}: {sorted(extra)}"
    )
    missing = all_expected - found_conf_files
    assert not missing, (
        f"Missing expected .conf files in {DEPLOYMENTS_DIR}: {sorted(missing)}"
    )


# ── Audit log ────────────────────────────────────────────────────────────────

def test_audit_log_exists():
    assert os.path.isfile(AUDIT_LOG), (
        f"Audit log does not exist at {AUDIT_LOG}. "
        "It should have been created after the key rotation."
    )


def test_audit_log_exact_content():
    with open(AUDIT_LOG, "r") as f:
        actual = f.read()
    assert actual == EXPECTED_AUDIT_CONTENT, (
        f"Audit log at {AUDIT_LOG} does not have the expected content.\n"
        f"Expected:\n{EXPECTED_AUDIT_CONTENT!r}\n"
        f"Actual:\n{actual!r}\n"
        "The log must contain exactly the three modified file paths, "
        "sorted alphabetically, one per line, with no extra whitespace or blank lines."
    )


def test_audit_log_lists_correct_files():
    """Check each expected file path is present in the audit log."""
    with open(AUDIT_LOG, "r") as f:
        lines = f.read().splitlines()

    expected_paths = sorted(MODIFIED_FILES.keys())
    assert lines == expected_paths, (
        f"Audit log lines do not match expected modified file paths.\n"
        f"Expected lines: {expected_paths}\n"
        f"Actual lines:   {lines}"
    )


def test_audit_log_sorted_alphabetically():
    with open(AUDIT_LOG, "r") as f:
        lines = f.read().splitlines()

    # Remove blank lines for this check
    non_blank = [l for l in lines if l.strip()]
    assert non_blank == sorted(non_blank), (
        f"Audit log entries are not sorted alphabetically.\n"
        f"Actual order:    {non_blank}\n"
        f"Expected order:  {sorted(non_blank)}"
    )


def test_audit_log_no_blank_lines():
    with open(AUDIT_LOG, "r") as f:
        content = f.read()

    lines = content.splitlines()
    blank_lines = [i + 1 for i, line in enumerate(lines) if line.strip() == ""]
    assert not blank_lines, (
        f"Audit log at {AUDIT_LOG} contains blank lines at line numbers: {blank_lines}\n"
        f"Actual content:\n{content!r}"
    )


def test_audit_log_no_trailing_whitespace_on_lines():
    with open(AUDIT_LOG, "r") as f:
        lines = f.read().splitlines()

    bad_lines = [
        (i + 1, repr(line))
        for i, line in enumerate(lines)
        if line != line.strip()
    ]
    assert not bad_lines, (
        f"Audit log at {AUDIT_LOG} has lines with leading/trailing whitespace:\n"
        + "\n".join(f"  Line {ln}: {val}" for ln, val in bad_lines)
    )


def test_audit_log_ends_with_newline():
    with open(AUDIT_LOG, "r") as f:
        content = f.read()
    assert content.endswith("\n"), (
        f"Audit log at {AUDIT_LOG} does not end with a newline character.\n"
        f"Actual content:\n{content!r}"
    )


def test_audit_log_no_trailing_blank_line():
    with open(AUDIT_LOG, "r") as f:
        content = f.read()
    # After stripping the single trailing newline, there should be no further newlines at the end
    stripped = content.rstrip("\n")
    assert "\n\n" not in content, (
        f"Audit log at {AUDIT_LOG} appears to have a trailing blank line.\n"
        f"Actual content:\n{content!r}"
    )
    # Confirm the last non-empty line is the last expected path
    lines = stripped.splitlines()
    expected_last = sorted(MODIFIED_FILES.keys())[-1]
    assert lines[-1] == expected_last, (
        f"The last line of the audit log should be '{expected_last}' "
        f"but got '{lines[-1]}'."
    )


def test_audit_log_only_lists_modified_files():
    """Ensure unmodified files are NOT listed in the audit log."""
    with open(AUDIT_LOG, "r") as f:
        content = f.read()

    for filepath in UNMODIFIED_FILES:
        assert filepath not in content, (
            f"Audit log incorrectly lists unmodified file: {filepath}\n"
            f"Only files where the old key was replaced should appear in the log.\n"
            f"Audit log content:\n{content!r}"
        )