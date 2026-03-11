# test_final_state.py

import os
import stat
import pytest

SCRIPT_PATH = "/home/user/workflows/process_orders.sh"


def get_script_contents():
    with open(SCRIPT_PATH, "r") as f:
        return f.read()


def test_script_exists():
    assert os.path.isfile(SCRIPT_PATH), (
        f"Script not found at {SCRIPT_PATH}. "
        "The fixed script must exist at this path."
    )


def test_script_is_executable():
    assert os.access(SCRIPT_PATH, os.X_OK), (
        f"Script at {SCRIPT_PATH} is not executable. "
        "The fixed script must retain execute permission (chmod +x)."
    )


def test_script_has_execute_permission_bit():
    st = os.stat(SCRIPT_PATH)
    mode = st.st_mode
    assert mode & stat.S_IXUSR, (
        f"Script at {SCRIPT_PATH} does not have user execute bit set. "
        "The script must be executable (chmod +x)."
    )


def test_no_hardcoded_temp_path():
    contents = get_script_contents()
    count = contents.count("/tmp/orders_temp.csv")
    assert count == 0, (
        f"Script at {SCRIPT_PATH} still contains {count} reference(s) to "
        "'/tmp/orders_temp.csv'. All occurrences of the hardcoded insecure "
        "temp path must be removed and replaced with $TMPFILE."
    )


def test_contains_mktemp_with_template():
    contents = get_script_contents()
    assert "mktemp /tmp/orders_tmp.XXXXXX" in contents, (
        f"Script at {SCRIPT_PATH} does not contain 'mktemp /tmp/orders_tmp.XXXXXX'. "
        "The fix must use mktemp with the exact template '/tmp/orders_tmp.XXXXXX'."
    )


def test_contains_tmpfile_assignment():
    contents = get_script_contents()
    assert "TMPFILE=$(mktemp /tmp/orders_tmp.XXXXXX)" in contents, (
        f"Script at {SCRIPT_PATH} does not contain "
        "'TMPFILE=$(mktemp /tmp/orders_tmp.XXXXXX)'. "
        "The mktemp result must be assigned to a variable named TMPFILE."
    )


def test_contains_trap_statement():
    contents = get_script_contents()
    assert 'trap "rm -f $TMPFILE" EXIT INT TERM' in contents, (
        f"Script at {SCRIPT_PATH} does not contain the required trap statement. "
        'Expected: trap "rm -f $TMPFILE" EXIT INT TERM\n'
        "The trap must handle EXIT, INT, and TERM signals to ensure cleanup."
    )


def test_trap_on_single_line():
    contents = get_script_contents()
    lines = contents.splitlines()
    trap_lines = [line for line in lines if 'trap "rm -f $TMPFILE" EXIT INT TERM' in line]
    assert len(trap_lines) >= 1, (
        f"Script at {SCRIPT_PATH} does not have the trap statement on a single line. "
        'The trap must appear as: trap "rm -f $TMPFILE" EXIT INT TERM'
    )


def test_trap_immediately_after_tmpfile_assignment():
    contents = get_script_contents()
    lines = contents.splitlines()
    tmpfile_assign_idx = None
    trap_idx = None
    for i, line in enumerate(lines):
        if "TMPFILE=$(mktemp /tmp/orders_tmp.XXXXXX)" in line:
            tmpfile_assign_idx = i
        if 'trap "rm -f $TMPFILE" EXIT INT TERM' in line:
            trap_idx = i
    assert tmpfile_assign_idx is not None, (
        f"Script at {SCRIPT_PATH} does not contain TMPFILE assignment."
    )
    assert trap_idx is not None, (
        f"Script at {SCRIPT_PATH} does not contain the trap statement."
    )
    assert trap_idx == tmpfile_assign_idx + 1, (
        f"Script at {SCRIPT_PATH}: trap statement is not immediately after "
        f"TMPFILE assignment. TMPFILE is on line {tmpfile_assign_idx + 1}, "
        f"trap is on line {trap_idx + 1}. The trap must follow immediately."
    )


def test_tmpfile_variable_used_multiple_times():
    contents = get_script_contents()
    count = contents.count("$TMPFILE")
    assert count >= 4, (
        f"Script at {SCRIPT_PATH} contains only {count} reference(s) to '$TMPFILE'. "
        "Expected at least 4 uses: trap, cat redirect, grep input, wc input, and rm. "
        "All former references to the hardcoded path must use $TMPFILE."
    )


def test_tmpfile_used_in_cat_redirect():
    contents = get_script_contents()
    assert "cat" in contents and "$TMPFILE" in contents, (
        f"Script at {SCRIPT_PATH} must use $TMPFILE as the cat redirect target."
    )
    lines = contents.splitlines()
    cat_lines = [line for line in lines if "cat" in line and "$TMPFILE" in line]
    assert len(cat_lines) >= 1, (
        f"Script at {SCRIPT_PATH} does not have a 'cat' command referencing $TMPFILE. "
        "The aggregation step must write to $TMPFILE."
    )


def test_tmpfile_used_in_grep():
    contents = get_script_contents()
    lines = contents.splitlines()
    grep_lines = [line for line in lines if "grep" in line and "$TMPFILE" in line]
    assert len(grep_lines) >= 1, (
        f"Script at {SCRIPT_PATH} does not have a 'grep' command referencing $TMPFILE. "
        "The grep filter step must read from $TMPFILE."
    )


def test_tmpfile_used_in_wc():
    contents = get_script_contents()
    lines = contents.splitlines()
    wc_lines = [line for line in lines if "wc" in line and "$TMPFILE" in line]
    assert len(wc_lines) >= 1, (
        f"Script at {SCRIPT_PATH} does not have a 'wc' command referencing $TMPFILE. "
        "The count step must read from $TMPFILE."
    )


def test_tmpfile_used_in_rm_cleanup():
    contents = get_script_contents()
    lines = contents.splitlines()
    rm_lines = [line for line in lines if "rm" in line and "$TMPFILE" in line]
    assert len(rm_lines) >= 1, (
        f"Script at {SCRIPT_PATH} does not have an 'rm' command referencing $TMPFILE. "
        "The cleanup step must remove $TMPFILE."
    )


def test_bare_temp_path_line_removed():
    contents = get_script_contents()
    lines = contents.splitlines()
    bare_path_lines = [
        line for line in lines
        if line.strip() == "/tmp/orders_temp.csv"
    ]
    assert len(bare_path_lines) == 0, (
        f"Script at {SCRIPT_PATH} still contains a bare '/tmp/orders_temp.csv' line. "
        "The accidental bare path line must be removed or replaced."
    )


def test_script_has_shebang():
    contents = get_script_contents()
    assert contents.startswith("#!/bin/bash"), (
        f"Script at {SCRIPT_PATH} does not start with '#!/bin/bash'. "
        "The shebang line must be preserved."
    )


def test_script_contains_set_e():
    contents = get_script_contents()
    assert "set -e" in contents, (
        f"Script at {SCRIPT_PATH} does not contain 'set -e'. "
        "The 'set -e' directive must be preserved."
    )


def test_script_contains_input_dir():
    contents = get_script_contents()
    assert 'INPUT_DIR="/home/user/data/orders"' in contents, (
        f"Script at {SCRIPT_PATH} does not contain the expected INPUT_DIR assignment. "
        "The script structure must remain intact after the fix."
    )


def test_script_contains_output_dir():
    contents = get_script_contents()
    assert 'OUTPUT_DIR="/home/user/data/processed"' in contents, (
        f"Script at {SCRIPT_PATH} does not contain the expected OUTPUT_DIR assignment. "
        "The script structure must remain intact after the fix."
    )


def test_script_contains_grep_cancelled():
    contents = get_script_contents()
    assert "grep -v" in contents and "CANCELLED" in contents, (
        f"Script at {SCRIPT_PATH} does not contain the expected grep -v CANCELLED command. "
        "The order filtering logic must be preserved."
    )


def test_script_contains_wc_count():
    contents = get_script_contents()
    assert "wc -l" in contents, (
        f"Script at {SCRIPT_PATH} does not contain 'wc -l'. "
        "The order count logic must be preserved."
    )


def test_script_contains_workflow_complete():
    contents = get_script_contents()
    assert "Workflow complete." in contents, (
        f"Script at {SCRIPT_PATH} does not contain 'Workflow complete.' message. "
        "The final echo statement must be preserved."
    )


def test_no_other_hardcoded_tmp_paths():
    contents = get_script_contents()
    # Ensure no variant of the old path sneaked back in
    assert "/tmp/orders_temp" not in contents, (
        f"Script at {SCRIPT_PATH} contains a reference to '/tmp/orders_temp' "
        "(possibly a variant of the old insecure path). "
        "All references to the old hardcoded temp path must be removed."
    )