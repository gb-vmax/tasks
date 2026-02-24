# test_final_state.py

import os
import pytest

HOME = "/home/user"
PROJECT_ALPHA = os.path.join(HOME, "project_alpha")
MAIN_PY = os.path.join(PROJECT_ALPHA, "main.py")
SCRIPTS_DIR = os.path.join(PROJECT_ALPHA, "scripts")
HELPER_SH = os.path.join(SCRIPTS_DIR, "helper.sh")
WORKSPACE_LINKS = os.path.join(HOME, "workspace_links")
ALPHA_MAIN_LINK = os.path.join(WORKSPACE_LINKS, "alpha_main.py")
ALPHA_HELPER_LINK = os.path.join(WORKSPACE_LINKS, "alpha_helper.sh")
SYMLINK_LOG = os.path.join(WORKSPACE_LINKS, "symlink_creation.log")

def test_workspace_links_directory_exists():
    assert os.path.isdir(WORKSPACE_LINKS), (
        f"Directory {WORKSPACE_LINKS} does not exist. "
        "You must create /home/user/workspace_links/."
    )

def test_alpha_main_symlink_correct():
    assert os.path.islink(ALPHA_MAIN_LINK), (
        f"{ALPHA_MAIN_LINK} is missing or not a symbolic link. "
        "You must create a symlink named 'alpha_main.py' in /home/user/workspace_links/."
    )
    target = os.readlink(ALPHA_MAIN_LINK)
    if not os.path.isabs(target):
        target = os.path.abspath(os.path.join(os.path.dirname(ALPHA_MAIN_LINK), target))
    assert target == MAIN_PY, (
        f"Symlink {ALPHA_MAIN_LINK} points to {target}, but should point to {MAIN_PY} using an absolute path."
    )
    assert os.path.isfile(ALPHA_MAIN_LINK), (
        f"Symlink {ALPHA_MAIN_LINK} does not point to a valid file."
    )

def test_alpha_helper_symlink_correct():
    assert os.path.islink(ALPHA_HELPER_LINK), (
        f"{ALPHA_HELPER_LINK} is missing or not a symbolic link. "
        "You must create a symlink named 'alpha_helper.sh' in /home/user/workspace_links/."
    )
    target = os.readlink(ALPHA_HELPER_LINK)
    if not os.path.isabs(target):
        target = os.path.abspath(os.path.join(os.path.dirname(ALPHA_HELPER_LINK), target))
    assert target == HELPER_SH, (
        f"Symlink {ALPHA_HELPER_LINK} points to {target}, but should point to {HELPER_SH} using an absolute path."
    )
    assert os.path.isfile(ALPHA_HELPER_LINK), (
        f"Symlink {ALPHA_HELPER_LINK} does not point to a valid file."
    )

def test_symlink_creation_log_exists():
    assert os.path.isfile(SYMLINK_LOG), (
        f"Missing log file: {SYMLINK_LOG}. "
        "You must create symlink_creation.log in /home/user/workspace_links/."
    )

def test_symlink_creation_log_contents_exact():
    assert os.path.isfile(SYMLINK_LOG), (
        f"Cannot check log contents, file does not exist: {SYMLINK_LOG}"
    )
    with open(SYMLINK_LOG, "r") as f:
        lines = f.read().splitlines()
    expected_lines = [
        f"alpha_main.py -> {MAIN_PY}",
        f"alpha_helper.sh -> {HELPER_SH}",
    ]
    # Ignore order, but require exactly two lines, no extras or blanks
    assert sorted(lines) == sorted(expected_lines), (
        f"symlink_creation.log must contain exactly these two lines (any order, no extra lines):\n"
        f"{expected_lines}\n"
        f"Actual contents:\n{lines}"
    )

def test_links_point_to_absolute_paths():
    # This test is redundant with the above, but makes the requirement explicit
    main_target = os.readlink(ALPHA_MAIN_LINK)
    helper_target = os.readlink(ALPHA_HELPER_LINK)
    assert os.path.isabs(main_target), (
        f"Symlink {ALPHA_MAIN_LINK} does not use an absolute path for its target: {main_target}"
    )
    assert os.path.isabs(helper_target), (
        f"Symlink {ALPHA_HELPER_LINK} does not use an absolute path for its target: {helper_target}"
    )

def test_workspace_links_contains_only_expected_files():
    expected = {"alpha_main.py", "alpha_helper.sh", "symlink_creation.log"}
    actual = set(os.listdir(WORKSPACE_LINKS))
    extra = actual - expected
    missing = expected - actual
    assert not missing, (
        f"Missing in /home/user/workspace_links/: {missing}"
    )
    assert not extra, (
        f"Unexpected files or directories in /home/user/workspace_links/: {extra}"
    )