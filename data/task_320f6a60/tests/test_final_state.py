# test_final_state.py

"""
Pytest suite to validate the FINAL state of the system after the symbolic link and permissions audit task.

Checks:
- All three symbolic links exist at their absolute paths and point to the correct targets.
- Each symlink is a symlink and displays permissions 'lrwxrwxrwx'.
- Each target file exists and has exactly the required permissions string.
- The audit report file exists at /home/user/audit_report.txt and contains exactly the correct content if and only if all checks pass.
- If any check fails, the report must contain the single line: 'Audit failed: Discrepancy found in symbolic links or permissions.'
- The report content is printed to the console.

If any check fails, the test failure message must be descriptive about what is wrong.
"""

import os
import stat
import pytest

HOME = "/home/user"
WORKSPACE = os.path.join(HOME, "workspace")
PROJECTS = os.path.join(HOME, "projects")
CONFIG = os.path.join(HOME, "config")
DATA = os.path.join(HOME, "data")

AUDIT_REPORT_PATH = os.path.join(HOME, "audit_report.txt")

# Specifications
SYMLINKS = [
    {
        "name": "project_link",
        "path": os.path.join(WORKSPACE, "project_link"),
        "target": os.path.join(PROJECTS, "main_project.txt"),
        "target_perms": "-rw-------",
    },
    {
        "name": "config_symlink",
        "path": os.path.join(WORKSPACE, "config_symlink"),
        "target": os.path.join(CONFIG, "settings.conf"),
        "target_perms": "-rw-r-----",
    },
    {
        "name": "data_link",
        "path": os.path.join(WORKSPACE, "data_link"),
        "target": os.path.join(DATA, "raw_dataset.csv"),
        "target_perms": "-rwxr-x---",
    },
]

CORRECT_REPORT = """Symbolic Link Audit Report
--------------------------
project_link: EXISTS, points to /home/user/projects/main_project.txt, perms: lrwxrwxrwx, target perms: -rw-------
config_symlink: EXISTS, points to /home/user/config/settings.conf, perms: lrwxrwxrwx, target perms: -rw-r-----
data_link: EXISTS, points to /home/user/data/raw_dataset.csv, perms: lrwxrwxrwx, target perms: -rwxr-x---
"""

FAILED_REPORT = "Audit failed: Discrepancy found in symbolic links or permissions."

def mode_to_str(mode, is_symlink=False):
    if is_symlink:
        # Symlinks always show as lrwxrwxrwx in ls -l, regardless of actual permissions
        return "lrwxrwxrwx"
    # File
    perms = []
    perms.append("-")
    perms.append("r" if mode & stat.S_IRUSR else "-")
    perms.append("w" if mode & stat.S_IWUSR else "-")
    perms.append("x" if mode & stat.S_IXUSR else "-")
    perms.append("r" if mode & stat.S_IRGRP else "-")
    perms.append("w" if mode & stat.S_IWGRP else "-")
    perms.append("x" if mode & stat.S_IXGRP else "-")
    perms.append("r" if mode & stat.S_IROTH else "-")
    perms.append("w" if mode & stat.S_IWOTH else "-")
    perms.append("x" if mode & stat.S_IXOTH else "-")
    return "".join(perms)

def resolve_symlink_absolute(link_path):
    """Return the absolute path that a symlink points to, resolving relative links correctly."""
    actual_target = os.readlink(link_path)
    if not os.path.isabs(actual_target):
        # Relative symlink: resolve from the directory of the link
        actual_target = os.path.abspath(os.path.join(os.path.dirname(link_path), actual_target))
    return os.path.normpath(actual_target)

def check_symlink_and_target(symlink_spec):
    link_path = symlink_spec["path"]
    target_path = symlink_spec["target"]
    expected_target_perms = symlink_spec["target_perms"]

    # 1. Symlink exists and is a symlink
    if not os.path.lexists(link_path):
        return f"Missing symlink: {link_path}"
    if not os.path.islink(link_path):
        return f"{link_path} exists but is not a symbolic link"

    # 2. Symlink points to correct absolute target
    actual_target = resolve_symlink_absolute(link_path)
    if actual_target != os.path.normpath(target_path):
        return f"{link_path} points to {actual_target}, expected {target_path}"

    # 3. Symlink "permissions" (lstat, not stat)
    try:
        st = os.lstat(link_path)
    except Exception as e:
        return f"Failed to lstat symlink {link_path}: {e}"
    perms_str = mode_to_str(st.st_mode, is_symlink=True)
    if perms_str != "lrwxrwxrwx":
        return f"Symlink {link_path} permissions are {perms_str}, expected lrwxrwxrwx"

    # 4. Target file exists
    if not os.path.isfile(target_path):
        return f"Target file does not exist: {target_path}"

    # 5. Target file permissions
    try:
        st_target = os.stat(target_path)
    except Exception as e:
        return f"Failed to stat target file {target_path}: {e}"
    target_perms_str = mode_to_str(st_target.st_mode)
    if target_perms_str != expected_target_perms:
        return (f"Target file {target_path} permissions are {target_perms_str}, "
                f"expected {expected_target_perms}")
    return None  # All OK

def collect_symlink_audit_lines():
    """Returns all lines for the valid audit report, in order."""
    lines = [
        "Symbolic Link Audit Report",
        "--------------------------",
    ]
    for symlink_spec in SYMLINKS:
        link_name = symlink_spec["name"]
        link_path = symlink_spec["path"]
        target_path = symlink_spec["target"]
        target_perms = symlink_spec["target_perms"]
        # Symlink perms always lrwxrwxrwx
        line = (
            f"{link_name}: EXISTS, points to {target_path}, perms: lrwxrwxrwx, target perms: {target_perms}"
        )
        lines.append(line)
    return "\n".join(lines) + "\n"

def test_symlinks_and_permissions_final_state():
    """
    Validate the full symlink structure, file permissions, and audit report.
    """
    errors = []
    for symlink_spec in SYMLINKS:
        err = check_symlink_and_target(symlink_spec)
        if err:
            errors.append(err)

    # Check audit report existence
    if not os.path.exists(AUDIT_REPORT_PATH):
        errors.append(f"Audit report file missing: {AUDIT_REPORT_PATH}")

    # Load report content (if present) for further checks
    report_content = None
    if os.path.exists(AUDIT_REPORT_PATH):
        try:
            with open(AUDIT_REPORT_PATH, "r", encoding="utf-8") as f:
                report_content = f.read()
        except Exception as e:
            errors.append(f"Could not read audit report file: {e}")

    # If everything else is correct, the report content must be exactly as specified
    if not errors:
        # Must match exactly the correct report
        if report_content != CORRECT_REPORT:
            errors.append("Audit report content does not match the required format/content for a successful audit.")

    else:
        # If there are errors, the report must contain only the failed string
        if report_content is not None and report_content.strip() != FAILED_REPORT:
            errors.append("Audit report content is incorrect for a failed audit (should only contain the failure message).")

    # Print the report content to the console, as required
    if report_content is not None:
        print(report_content, end="")  # Don't add extra newline

    if errors:
        pytest.fail(
            "Final state validation failed:\n" +
            "\n".join(f"- {error}" for error in errors)
        )