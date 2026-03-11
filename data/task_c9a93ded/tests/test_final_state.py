# test_final_state.py

import os
import subprocess
import pytest

PIPELINE_DIR = "/home/user/pipeline"
SCRIPT_PATH = "/home/user/pipeline/check_apk_sizes.py"
APKS_DIR = "/home/user/pipeline/apks"
REPORT_PATH = "/home/user/pipeline/size_report.txt"

APK_FILES = {
    "app-debug.apk": 1048576,
    "app-release.apk": 2097152,
    "app-staging.apk": 524288,
}

EXPECTED_REPORT = (
    "app-debug.apk: 1024 KB\n"
    "app-release.apk: 2048 KB\n"
    "app-staging.apk: 512 KB\n"
    "---\n"
    "Total: 3584 KB\n"
)


# ---------------------------------------------------------------------------
# Script file checks
# ---------------------------------------------------------------------------

def test_script_exists():
    assert os.path.isfile(SCRIPT_PATH), (
        f"Script {SCRIPT_PATH} does not exist."
    )


def test_script_is_valid_python3():
    """The script must parse without errors under Python 3."""
    result = subprocess.run(
        ["python3", "-c", f"import ast; ast.parse(open('{SCRIPT_PATH}').read())"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"Script {SCRIPT_PATH} does not parse as valid Python 3.\n"
        f"stderr: {result.stderr}"
    )


def test_script_has_no_bare_print_statements():
    """Bare `print` statements (Python 2 style) must have been fixed."""
    with open(SCRIPT_PATH, "r") as f:
        lines = f.readlines()

    bare_print_lines = []
    for lineno, line in enumerate(lines, start=1):
        stripped = line.strip()
        # A bare print statement looks like:  print "..." or print '...'
        # It does NOT look like: print(...)
        if stripped.startswith("print ") or stripped.startswith('print"') or stripped.startswith("print'"):
            bare_print_lines.append((lineno, line.rstrip()))

    assert not bare_print_lines, (
        f"Script {SCRIPT_PATH} still contains Python 2 bare print statements:\n"
        + "\n".join(f"  Line {ln}: {txt}" for ln, txt in bare_print_lines)
    )


def test_script_uses_integer_division():
    """The division `size_bytes / 1024` should be `//` to avoid float accumulation."""
    with open(SCRIPT_PATH, "r") as f:
        content = f.read()

    # The fix requires integer division for correct KB calculation
    assert "size_bytes // 1024" in content or "size_bytes//1024" in content, (
        f"Script {SCRIPT_PATH} does not use integer division (`//`) for KB calculation. "
        f"The expression `size_bytes / 1024` produces a float in Python 3, which would "
        f"cause incorrect output. Please change it to `size_bytes // 1024`."
    )


def test_script_preserves_get_apk_sizes_function():
    with open(SCRIPT_PATH, "r") as f:
        content = f.read()
    assert "def get_apk_sizes" in content, (
        f"Script {SCRIPT_PATH} is missing the `get_apk_sizes` function — "
        f"only minimal fixes should have been applied."
    )


def test_script_preserves_apk_scanning_logic():
    with open(SCRIPT_PATH, "r") as f:
        content = f.read()
    assert ".apk" in content, (
        f"Script {SCRIPT_PATH} no longer scans for .apk files."
    )
    assert "os.path.getsize" in content, (
        f"Script {SCRIPT_PATH} no longer uses os.path.getsize."
    )
    assert "Total" in content, (
        f"Script {SCRIPT_PATH} no longer outputs a 'Total' line."
    )
    assert "---" in content, (
        f"Script {SCRIPT_PATH} no longer outputs the '---' separator."
    )


# ---------------------------------------------------------------------------
# APK files sanity checks (must still be intact)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("apk_name,expected_size", APK_FILES.items())
def test_apk_file_exists(apk_name, expected_size):
    apk_path = os.path.join(APKS_DIR, apk_name)
    assert os.path.isfile(apk_path), (
        f"APK file {apk_path} does not exist."
    )


@pytest.mark.parametrize("apk_name,expected_size", APK_FILES.items())
def test_apk_file_size(apk_name, expected_size):
    apk_path = os.path.join(APKS_DIR, apk_name)
    actual_size = os.path.getsize(apk_path)
    assert actual_size == expected_size, (
        f"APK file {apk_path} has size {actual_size} bytes, "
        f"expected {expected_size} bytes."
    )


# ---------------------------------------------------------------------------
# Script execution check
# ---------------------------------------------------------------------------

def test_script_runs_successfully_under_python3():
    """Running the fixed script with python3 must exit with code 0."""
    result = subprocess.run(
        ["python3", SCRIPT_PATH, APKS_DIR],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"Script {SCRIPT_PATH} exited with code {result.returncode} when run under Python 3.\n"
        f"stdout: {result.stdout}\n"
        f"stderr: {result.stderr}"
    )


def test_script_stdout_matches_expected():
    """The script's stdout must match the expected report format exactly."""
    result = subprocess.run(
        ["python3", SCRIPT_PATH, APKS_DIR],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"Script exited with code {result.returncode}.\nstderr: {result.stderr}"
    )
    assert result.stdout == EXPECTED_REPORT, (
        f"Script stdout does not match expected output.\n"
        f"Expected:\n{EXPECTED_REPORT!r}\n"
        f"Got:\n{result.stdout!r}"
    )


# ---------------------------------------------------------------------------
# Size report file checks
# ---------------------------------------------------------------------------

def test_size_report_exists():
    assert os.path.isfile(REPORT_PATH), (
        f"Size report {REPORT_PATH} does not exist. "
        f"The script must have been run and its output redirected to this file."
    )


def test_size_report_is_not_empty():
    size = os.path.getsize(REPORT_PATH)
    assert size > 0, (
        f"Size report {REPORT_PATH} exists but is empty."
    )


def test_size_report_exact_contents():
    """The report file must contain exactly the expected output."""
    with open(REPORT_PATH, "r") as f:
        actual = f.read()

    assert actual == EXPECTED_REPORT, (
        f"Contents of {REPORT_PATH} do not match expected output.\n"
        f"Expected:\n{EXPECTED_REPORT!r}\n"
        f"Got:\n{actual!r}"
    )


def test_size_report_line_count():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    # 3 APK lines + 1 separator + 1 total = 5 lines
    assert len(lines) == 5, (
        f"Expected 5 lines in {REPORT_PATH} (3 APK lines, '---', 'Total: ...'), "
        f"but found {len(lines)} lines:\n" + "".join(lines)
    )


def test_size_report_apk_lines():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    expected_apk_lines = [
        "app-debug.apk: 1024 KB\n",
        "app-release.apk: 2048 KB\n",
        "app-staging.apk: 512 KB\n",
    ]
    for i, expected_line in enumerate(expected_apk_lines):
        assert lines[i] == expected_line, (
            f"Line {i+1} of {REPORT_PATH} is wrong.\n"
            f"Expected: {expected_line!r}\n"
            f"Got:      {lines[i]!r}"
        )


def test_size_report_separator_line():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    assert lines[3] == "---\n", (
        f"Line 4 of {REPORT_PATH} (separator) is wrong.\n"
        f"Expected: '---\\n'\n"
        f"Got:      {lines[3]!r}"
    )


def test_size_report_total_line():
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    assert lines[4] == "Total: 3584 KB\n", (
        f"Line 5 of {REPORT_PATH} (total) is wrong.\n"
        f"Expected: 'Total: 3584 KB\\n'\n"
        f"Got:      {lines[4]!r}"
    )


def test_size_report_ends_with_newline():
    with open(REPORT_PATH, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"File {REPORT_PATH} does not end with a newline character."
    )


def test_size_report_alphabetical_order():
    """APK entries must be sorted alphabetically by filename."""
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    apk_lines = [l.strip() for l in lines[:3]]
    filenames = [l.split(":")[0] for l in apk_lines]
    assert filenames == sorted(filenames), (
        f"APK entries in {REPORT_PATH} are not sorted alphabetically.\n"
        f"Found order: {filenames}\n"
        f"Expected order: {sorted(filenames)}"
    )


def test_size_report_total_is_sum_of_parts():
    """The Total KB must equal the sum of the individual KB values."""
    with open(REPORT_PATH, "r") as f:
        lines = f.readlines()

    kb_values = []
    for line in lines[:3]:
        # format: "filename.apk: NNN KB"
        parts = line.strip().split(": ")
        assert len(parts) == 2, (
            f"Unexpected line format in {REPORT_PATH}: {line!r}"
        )
        kb_str = parts[1].replace(" KB", "")
        kb_values.append(int(kb_str))

    total_line = lines[4].strip()
    total_str = total_line.replace("Total: ", "").replace(" KB", "")
    reported_total = int(total_str)
    expected_total = sum(kb_values)

    assert reported_total == expected_total, (
        f"Total in {REPORT_PATH} is {reported_total} KB, "
        f"but the sum of individual KB values is {expected_total} KB."
    )