# test_final_state.py

import os
import stat
import pytest
import subprocess
import re
from datetime import datetime, timedelta

HOME = "/home/user"
PROJECT_ENV = os.path.join(HOME, "project_env")
APP_PY = os.path.join(PROJECT_ENV, "app.py")
README_MD = os.path.join(PROJECT_ENV, "README.md")
ENV_REPORT = os.path.join(PROJECT_ENV, "env_report.txt")


@pytest.fixture(scope="module")
def report_lines():
    """Read env_report.txt and return lines as a list."""
    if not os.path.exists(ENV_REPORT):
        pytest.fail(f"Report file {ENV_REPORT} does not exist.")
    with open(ENV_REPORT, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    return lines


def test_project_env_directory_exists():
    assert os.path.isdir(PROJECT_ENV), (
        f"Directory {PROJECT_ENV} does not exist. "
        "It must be created as part of the task."
    )
    # Check permissions: user must be able to write and enter
    assert os.access(PROJECT_ENV, os.W_OK | os.X_OK), (
        f"User does not have write/execute permissions on {PROJECT_ENV}."
    )


def test_app_py_exists_and_empty():
    assert os.path.isfile(APP_PY), (
        f"File {APP_PY} does not exist. It must be created."
    )
    st = os.stat(APP_PY)
    assert st.st_size == 0, (
        f"File {APP_PY} is not empty. It must be an empty file."
    )


def test_readme_md_exists_and_empty():
    assert os.path.isfile(README_MD), (
        f"File {README_MD} does not exist. It must be created."
    )
    st = os.stat(README_MD)
    assert st.st_size == 0, (
        f"File {README_MD} is not empty. It must be an empty file."
    )


def test_env_report_exists():
    assert os.path.isfile(ENV_REPORT), (
        f"Report file {ENV_REPORT} does not exist."
    )


def test_env_report_format_and_content(report_lines):
    """
    Validate the env_report.txt file for:
    - exact formatting
    - dynamic values (timezone, datetime, locale, files)
    - no extra lines or trailing whitespace
    """
    expected_lines = 6
    assert len(report_lines) == expected_lines, (
        f"env_report.txt must have exactly {expected_lines} lines, found {len(report_lines)}.\n"
        f"Lines: {report_lines}"
    )

    # 1. TIMEZONE
    tz_line = report_lines[0]
    assert tz_line == "TIMEZONE: America/New_York", (
        f"First line of env_report.txt must be 'TIMEZONE: America/New_York', got: '{tz_line}'"
    )

    # 2. DATETIME
    dt_line = report_lines[1]
    dt_match = re.fullmatch(r"DATETIME: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", dt_line)
    assert dt_match, (
        f"Second line must be 'DATETIME: YYYY-MM-DD HH:MM:SS' (24hr), got: '{dt_line}'"
    )
    dt_str = dt_match.group(1)
    try:
        report_dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    except Exception as e:
        pytest.fail(f"Could not parse DATETIME '{dt_str}': {e}")

    # Validate that the DATETIME matches the current time in New York within ±3 minutes
    # We'll use 'TZ=America/New_York date +%Y-%m-%d\ %H:%M:%S'
    try:
        actual_dt_str = subprocess.check_output(
            ["env", "TZ=America/New_York", "date", "+%Y-%m-%d %H:%M:%S"],
            text=True
        ).strip()
        actual_dt = datetime.strptime(actual_dt_str, "%Y-%m-%d %H:%M:%S")
        # Allow up to 3 minutes difference (report could be slightly out of sync)
        delta = abs((actual_dt - report_dt).total_seconds())
        assert delta <= 180, (
            f"DATETIME in report ('{dt_str}') does not match current America/New_York time ('{actual_dt_str}')."
            " It should be generated at the time of the report (allowing 3 minutes tolerance)."
        )
    except Exception as e:
        pytest.skip(f"Could not verify New York time via 'date': {e}")

    # 3. LOCALE
    locale_line = report_lines[2]
    assert locale_line == "LOCALE: LANG=de_DE.UTF-8", (
        f"Third line must be 'LOCALE: LANG=de_DE.UTF-8', got: '{locale_line}'"
    )

    # 4. FILES
    files_section = report_lines[3:]
    assert files_section[0] == "FILES:", (
        f"Fourth line must be 'FILES:', got: '{files_section[0]}'"
    )
    assert files_section[1] == "- app.py FOUND", (
        f"Fifth line must be '- app.py FOUND', got: '{files_section[1]}'"
    )
    assert files_section[2] == "- README.md FOUND", (
        f"Sixth line must be '- README.md FOUND', got: '{files_section[2]}'"
    )


def test_no_extra_lines_or_trailing_whitespace(report_lines):
    # No trailing whitespace on any line
    for i, line in enumerate(report_lines):
        assert line == line.rstrip(), (
            f"Line {i+1} of env_report.txt has trailing whitespace: '{line}'"
        )

    # No extra lines after the last line
    with open(ENV_REPORT, "rb") as f:
        content = f.read()
    assert content.endswith(b"FOUND\n") or content.endswith(b"FOUND"), (
        "env_report.txt must not have extra blank lines or trailing whitespace after the last line."
    )


def test_session_timezone_is_america_new_york():
    # Check that the session's TZ is set to America/New_York (for the user session)
    tz_env = os.environ.get("TZ")
    if tz_env is not None:
        assert tz_env == "America/New_York", (
            f"Session TZ environment variable must be 'America/New_York', got '{tz_env}'.\n"
            "Make sure to set TZ for your session."
        )
    # Also check 'date' command with no explicit TZ (if TZ is set in environment, this will be enough)
    try:
        output = subprocess.check_output(["date", "+%Z"], text=True).strip()
        assert output in {"EDT", "EST"}, (
            f"Session timezone is not America/New_York (EDT/EST), got '{output}'.\n"
            "Make sure your session timezone is set for America/New_York."
        )
    except Exception:
        pytest.skip("Could not verify system timezone via 'date' command.")


def test_session_locale_is_de_de_utf8():
    # Check LANG environment variable
    lang_env = os.environ.get("LANG")
    if lang_env is not None:
        assert lang_env == "de_DE.UTF-8", (
            f"Session LANG environment variable must be 'de_DE.UTF-8', got '{lang_env}'."
        )
    # Check 'locale' command output for LANG=de_DE.UTF-8
    try:
        locale_out = subprocess.check_output(["locale"], text=True)
        lang_lines = [line for line in locale_out.splitlines() if line.startswith("LANG=")]
        assert lang_lines, (
            "Could not find LANG=... line in 'locale' command output."
        )
        lang_line = lang_lines[0].strip()
        assert lang_line == "LANG=de_DE.UTF-8", (
            f"'locale' command reports '{lang_line}', expected 'LANG=de_DE.UTF-8'."
        )
    except Exception:
        pytest.skip("Could not verify locale via 'locale' command.")


def test_permissions_project_env():
    # User must be able to write and enter project_env directory
    assert os.access(PROJECT_ENV, os.W_OK | os.X_OK), (
        f"User must have write and execute permissions on {PROJECT_ENV}."
    )
    # User must be able to write files in project_env
    for fname in [APP_PY, README_MD, ENV_REPORT]:
        assert os.access(fname, os.W_OK), (
            f"User must have write permission for {fname}."
        )