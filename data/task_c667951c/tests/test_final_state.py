# test_final_state.py

import os
import pytest

COMPLIANCE_SYMLINKS_DIR = "/home/user/compliance_symlinks"
AUDIT_LOG_PATH = "/home/user/symlink_audit.log"

EXPECTED_SYMLINKS = {
    "app.cfg": "/etc/app/config.cfg",
    "db.conf": "/var/db/db1.conf",
    "legacy.data": "/home/user/old/datafile",
}

EXPECTED_AUDIT_CONTENT = (
    "app.cfg -> /etc/app/config.cfg\n"
    "db.conf -> /var/db/db1.conf\n"
    "legacy.data -> /home/user/old/datafile\n"
)

def test_compliance_symlinks_dir_exists():
    assert os.path.isdir(COMPLIANCE_SYMLINKS_DIR), (
        f"Directory {COMPLIANCE_SYMLINKS_DIR} is missing. "
        "It must exist after the task is completed."
    )

def test_compliance_symlinks_contents_unchanged():
    """Check that the directory contains exactly the expected symlinks and nothing else."""
    entries = os.listdir(COMPLIANCE_SYMLINKS_DIR)
    symlinks = {name for name in entries if os.path.islink(os.path.join(COMPLIANCE_SYMLINKS_DIR, name))}
    missing = set(EXPECTED_SYMLINKS) - symlinks
    extra = symlinks - set(EXPECTED_SYMLINKS)
    assert not missing, (
        f"These expected symlinks are missing in {COMPLIANCE_SYMLINKS_DIR}: {sorted(missing)}"
    )
    assert not extra, (
        f"Found unexpected symlinks in {COMPLIANCE_SYMLINKS_DIR}: {sorted(extra)}"
    )
    # Also check for non-symlink files
    non_symlinks = [name for name in entries if not os.path.islink(os.path.join(COMPLIANCE_SYMLINKS_DIR, name))]
    assert not non_symlinks, (
        f"Found non-symlink entries in {COMPLIANCE_SYMLINKS_DIR}: {sorted(non_symlinks)}. "
        "Only symlinks should be present."
    )

@pytest.mark.parametrize("symlink,expected_target", sorted(EXPECTED_SYMLINKS.items()))
def test_symlink_targets_unchanged(symlink, expected_target):
    symlink_path = os.path.join(COMPLIANCE_SYMLINKS_DIR, symlink)
    assert os.path.islink(symlink_path), (
        f"{symlink_path} is missing or is not a symlink."
    )
    actual_target = os.readlink(symlink_path)
    assert actual_target == expected_target, (
        f"Symlink {symlink_path} points to {actual_target}, "
        f"but expected {expected_target}."
    )

def test_audit_log_exists():
    assert os.path.isfile(AUDIT_LOG_PATH), (
        f"Expected audit log file {AUDIT_LOG_PATH} does not exist."
    )

def test_audit_log_content_exact():
    assert os.path.isfile(AUDIT_LOG_PATH), (
        f"Expected audit log file {AUDIT_LOG_PATH} does not exist."
    )
    with open(AUDIT_LOG_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == EXPECTED_AUDIT_CONTENT, (
        f"{AUDIT_LOG_PATH} content is incorrect.\n"
        f"Expected exactly:\n{EXPECTED_AUDIT_CONTENT!r}\n"
        f"But got:\n{content!r}\n"
        "Check that you output one line per symlink, sorted lexicographically by symlink name, "
        "with no blank lines, extra lines, or comments."
    )

def test_audit_log_line_count():
    with open(AUDIT_LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    assert len(lines) == 3, (
        f"{AUDIT_LOG_PATH} should contain exactly 3 lines, one per symlink. "
        f"Found {len(lines)} lines."
    )
    for idx, line in enumerate(lines):
        assert line.strip(), (
            f"Line {idx+1} in {AUDIT_LOG_PATH} is blank. "
            "There should be no blank lines."
        )

def test_audit_log_no_extra_files_in_dir():
    """Ensure no extra files were created in the symlink directory."""
    entries = os.listdir(COMPLIANCE_SYMLINKS_DIR)
    non_symlinks = [name for name in entries if not os.path.islink(os.path.join(COMPLIANCE_SYMLINKS_DIR, name))]
    assert not non_symlinks, (
        f"Found non-symlink entries in {COMPLIANCE_SYMLINKS_DIR}: {sorted(non_symlinks)}. "
        "Only symlinks should be present; do not write the audit log here."
    )

def test_legacy_data_symlink_points_to_missing_file():
    """Specifically check that the legacy.data symlink points to a non-existent file."""
    symlink_path = os.path.join(COMPLIANCE_SYMLINKS_DIR, "legacy.data")
    target_path = os.readlink(symlink_path)
    assert not os.path.exists(target_path), (
        f"The target of {symlink_path} ('{target_path}') unexpectedly exists. "
        "It should not exist."
    )