# test_final_state.py

import os
import stat
import pytest

PROVISIONING_DIR = "/home/user/provisioning"
PROVISION_SH = "/home/user/provisioning/provision.sh"
ENV_CONF = "/home/user/provisioning/env.conf"
RUN_LOG = "/home/user/provisioning/run.log"
REPORT_TXT = "/home/user/provisioning/report.txt"

EXPECTED_LOG_CONTENTS = """\
[START] Provisioning environment: staging in us-east-1
[INFO] Services to provision: nginx,postgres,redis
[INFO] Setting up nginx...
[DONE] nginx provisioned successfully
[INFO] Setting up postgres...
[DONE] postgres provisioned successfully
[INFO] Setting up redis...
[DONE] redis provisioned successfully
[END] All services provisioned
"""

EXPECTED_REPORT_CONTENTS = """\
=== PROVISIONING REPORT ===
Config: /home/user/provisioning/env.conf
Exit code: 0
Lines logged: 9
Services provisioned: 3

--- LOG ---
[START] Provisioning environment: staging in us-east-1
[INFO] Services to provision: nginx,postgres,redis
[INFO] Setting up nginx...
[DONE] nginx provisioned successfully
[INFO] Setting up postgres...
[DONE] postgres provisioned successfully
[INFO] Setting up redis...
[DONE] redis provisioned successfully
[END] All services provisioned
"""


def test_provision_sh_exists():
    assert os.path.isfile(PROVISION_SH), (
        f"{PROVISION_SH} does not exist. The provisioning script must be present."
    )


def test_provision_sh_is_executable():
    """provision.sh must have execute permission set."""
    file_stat = os.stat(PROVISION_SH)
    mode = file_stat.st_mode
    is_executable = bool(mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))
    assert is_executable, (
        f"{PROVISION_SH} is not executable. "
        "The student must set execute permission on the script (e.g., chmod +x)."
    )


def test_provision_sh_not_modified():
    """provision.sh must not have been modified."""
    with open(PROVISION_SH, "r") as f:
        contents = f.read()

    assert "#!/bin/bash" in contents, (
        f"{PROVISION_SH} does not contain '#!/bin/bash'. The script may have been modified."
    )
    assert "CONFIG=$1" in contents, (
        f"{PROVISION_SH} does not contain 'CONFIG=$1'. The script may have been modified."
    )
    assert "[DONE]" in contents, (
        f"{PROVISION_SH} does not contain '[DONE]'. The script may have been modified."
    )
    assert 'source "$CONFIG"' in contents, (
        f"{PROVISION_SH} does not contain 'source \"$CONFIG\"'. The script may have been modified."
    )


def test_env_conf_not_modified():
    """env.conf must not have been modified."""
    with open(ENV_CONF, "r") as f:
        contents = f.read().strip()

    expected_lines = [
        "ENV=staging",
        "REGION=us-east-1",
        "SERVICES=nginx,postgres,redis",
    ]
    for line in expected_lines:
        assert line in contents, (
            f"{ENV_CONF} does not contain expected line: '{line}'. "
            f"The config file may have been modified. Actual contents:\n{contents}"
        )


def test_run_log_exists():
    assert os.path.isfile(RUN_LOG), (
        f"{RUN_LOG} does not exist. "
        "The student must capture the script's stdout into run.log."
    )


def test_run_log_contents():
    with open(RUN_LOG, "r") as f:
        contents = f.read()

    assert contents == EXPECTED_LOG_CONTENTS, (
        f"{RUN_LOG} does not contain the expected contents.\n"
        f"Expected:\n{EXPECTED_LOG_CONTENTS!r}\n"
        f"Actual:\n{contents!r}"
    )


def test_run_log_line_count():
    with open(RUN_LOG, "r") as f:
        lines = f.readlines()

    # Count non-empty trailing: the file should have exactly 9 lines
    # Each line ends with \n, so splitlines gives 9 entries
    line_count = len(contents_as_lines(RUN_LOG))
    assert line_count == 9, (
        f"{RUN_LOG} has {line_count} lines, but expected 9 lines. "
        f"Ensure the script output is captured correctly."
    )


def contents_as_lines(filepath):
    """Return lines as produced by the script (splitlines preserving all lines)."""
    with open(filepath, "r") as f:
        content = f.read()
    return content.splitlines()


def test_run_log_done_lines():
    lines = contents_as_lines(RUN_LOG)
    done_lines = [line for line in lines if line.startswith("[DONE]")]
    assert len(done_lines) == 3, (
        f"{RUN_LOG} has {len(done_lines)} lines starting with '[DONE]', but expected 3. "
        f"Lines found: {done_lines}"
    )


def test_report_txt_exists():
    assert os.path.isfile(REPORT_TXT), (
        f"{REPORT_TXT} does not exist. "
        "The student must create the final report file."
    )


def test_report_txt_contents():
    with open(REPORT_TXT, "r") as f:
        contents = f.read()

    assert contents == EXPECTED_REPORT_CONTENTS, (
        f"{REPORT_TXT} does not contain the expected contents.\n"
        f"Expected:\n{EXPECTED_REPORT_CONTENTS!r}\n"
        f"Actual:\n{contents!r}"
    )


def test_report_header_line():
    with open(REPORT_TXT, "r") as f:
        lines = f.readlines()

    assert lines[0].rstrip("\n") == "=== PROVISIONING REPORT ===", (
        f"First line of {REPORT_TXT} is not '=== PROVISIONING REPORT ==='. "
        f"Got: {lines[0]!r}"
    )


def test_report_config_line():
    with open(REPORT_TXT, "r") as f:
        contents = f.read()

    assert "Config: /home/user/provisioning/env.conf" in contents, (
        f"{REPORT_TXT} does not contain 'Config: /home/user/provisioning/env.conf'. "
        f"Actual contents:\n{contents}"
    )


def test_report_exit_code_line():
    with open(REPORT_TXT, "r") as f:
        contents = f.read()

    assert "Exit code: 0" in contents, (
        f"{REPORT_TXT} does not contain 'Exit code: 0'. "
        f"Actual contents:\n{contents}"
    )


def test_report_lines_logged():
    with open(REPORT_TXT, "r") as f:
        contents = f.read()

    assert "Lines logged: 9" in contents, (
        f"{REPORT_TXT} does not contain 'Lines logged: 9'. "
        f"Actual contents:\n{contents}"
    )


def test_report_services_provisioned():
    with open(REPORT_TXT, "r") as f:
        contents = f.read()

    assert "Services provisioned: 3" in contents, (
        f"{REPORT_TXT} does not contain 'Services provisioned: 3'. "
        f"Actual contents:\n{contents}"
    )


def test_report_log_section_separator():
    with open(REPORT_TXT, "r") as f:
        contents = f.read()

    assert "--- LOG ---" in contents, (
        f"{REPORT_TXT} does not contain '--- LOG ---' separator. "
        f"Actual contents:\n{contents}"
    )


def test_report_contains_full_log():
    with open(REPORT_TXT, "r") as f:
        report_contents = f.read()

    with open(RUN_LOG, "r") as f:
        log_contents = f.read()

    assert log_contents in report_contents, (
        f"The full contents of {RUN_LOG} are not present verbatim in {REPORT_TXT}. "
        f"Log contents:\n{log_contents!r}\n"
        f"Report contents:\n{report_contents!r}"
    )


def test_report_log_section_placement():
    """Verify that the log content appears after the --- LOG --- separator."""
    with open(REPORT_TXT, "r") as f:
        contents = f.read()

    separator = "--- LOG ---\n"
    sep_index = contents.find(separator)
    assert sep_index != -1, (
        f"Could not find '--- LOG ---\\n' in {REPORT_TXT}."
    )

    after_separator = contents[sep_index + len(separator):]
    expected_log = EXPECTED_LOG_CONTENTS

    assert after_separator == expected_log, (
        f"Content after '--- LOG ---' in {REPORT_TXT} does not match expected log.\n"
        f"Expected:\n{expected_log!r}\n"
        f"Actual:\n{after_separator!r}"
    )


def test_report_blank_line_before_log_section():
    """There should be a blank line between the stats section and --- LOG ---."""
    with open(REPORT_TXT, "r") as f:
        contents = f.read()

    assert "\n\n--- LOG ---" in contents, (
        f"{REPORT_TXT} does not have a blank line before '--- LOG ---'. "
        f"Expected a blank line separating the stats from the log section."
    )


def test_provisioning_dir_files_unchanged():
    """Only expected files should be in the provisioning directory."""
    expected_files = {"provision.sh", "env.conf", "run.log", "report.txt"}
    actual_files = set(os.listdir(PROVISIONING_DIR))
    unexpected = actual_files - expected_files
    # We don't fail on extra files, but we do ensure the expected ones exist
    for expected in expected_files:
        assert expected in actual_files, (
            f"Expected file '{expected}' not found in {PROVISIONING_DIR}. "
            f"Files present: {actual_files}"
        )