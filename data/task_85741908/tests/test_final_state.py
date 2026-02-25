# test_final_state.py

import os
import pwd
import grp
import stat
import pytest

ALICE_USERNAME = "alice"
DEVOPS_GROUP = "devops"
ALICE_HOME = "/home/alice"
ALICE_PROJECTS = "/home/alice/projects"
ALICE_NOTICE = "/home/alice/security_notice.txt"
LOG_PATH = "/home/user/hardening_log.txt"
USER_HOME = "/home/user"

SECURITY_NOTICE_CONTENT = (
    "SECURITY NOTICE:\n"
    "All access to this system is monitored.\n"
)

HARDENING_LOG_CONTENT = (
    "[STEP 1] Group 'devops' created.\n"
    "[STEP 2] User 'alice' created with group 'devops', home '/home/alice', shell '/bin/bash'.\n"
    "[STEP 3] Directory '/home/alice' permissions set to 700.\n"
    "[STEP 4] Directory '/home/alice/projects' created, permissions set to 770, group 'devops'.\n"
    "[STEP 5] File '/home/alice/security_notice.txt' created with owner-only permissions (600).\n"
)

def get_user(username):
    try:
        return pwd.getpwnam(username)
    except KeyError:
        return None

def get_group(groupname):
    try:
        return grp.getgrnam(groupname)
    except KeyError:
        return None

def get_file_stat(path):
    try:
        return os.stat(path)
    except FileNotFoundError:
        return None

@pytest.mark.describe("Final system state after hardening steps")
class TestFinalState:

    def test_group_devops_exists(self):
        """The group 'devops' must exist."""
        group = get_group(DEVOPS_GROUP)
        assert group is not None, "Group 'devops' does not exist."
        # No further GID check; system assigns dynamically

    def test_user_alice_exists_and_group(self):
        """The user 'alice' must exist with correct primary group and no supplementary groups."""
        alice = get_user(ALICE_USERNAME)
        assert alice is not None, "User 'alice' does not exist."
        group = get_group(DEVOPS_GROUP)
        assert group is not None, "Group 'devops' does not exist (needed for alice's group check)."
        assert alice.pw_gid == group.gr_gid, (
            f"User 'alice' primary group is not 'devops' (expected GID {group.gr_gid}, got {alice.pw_gid})."
        )
        # Check that alice is NOT in any other supplementary group
        groups_for_alice = [g.gr_name for g in grp.getgrall() if ALICE_USERNAME in g.gr_mem]
        assert groups_for_alice == [], (
            f"User 'alice' is a member of supplementary groups: {groups_for_alice}. She must ONLY be in 'devops' as primary group."
        )

    def test_user_alice_home_and_shell(self):
        """alice's home directory and shell must be set correctly."""
        alice = get_user(ALICE_USERNAME)
        assert alice is not None, "User 'alice' does not exist."
        assert alice.pw_dir == ALICE_HOME, (
            f"User 'alice' home directory is '{alice.pw_dir}', expected '{ALICE_HOME}'."
        )
        assert alice.pw_shell == "/bin/bash", (
            f"User 'alice' shell is '{alice.pw_shell}', expected '/bin/bash'."
        )

    def test_alice_home_dir_permissions(self):
        """The directory /home/alice must exist, owned by alice:devops, permissions 700."""
        st = get_file_stat(ALICE_HOME)
        assert st is not None, f"Directory '{ALICE_HOME}' does not exist."

        alice = get_user(ALICE_USERNAME)
        group = get_group(DEVOPS_GROUP)
        assert st.st_uid == alice.pw_uid, (
            f"Directory '{ALICE_HOME}' is not owned by user 'alice'."
        )
        assert st.st_gid == group.gr_gid, (
            f"Directory '{ALICE_HOME}' is not group-owned by 'devops'."
        )
        mode = stat.S_IMODE(st.st_mode)
        assert mode == 0o700, (
            f"Directory '{ALICE_HOME}' permissions are {oct(mode)}, expected 0o700 (drwx------)."
        )

    def test_alice_projects_dir(self):
        """The directory /home/alice/projects must exist, owned by alice:devops, permissions 770."""
        st = get_file_stat(ALICE_PROJECTS)
        assert st is not None, f"Directory '{ALICE_PROJECTS}' does not exist."

        alice = get_user(ALICE_USERNAME)
        group = get_group(DEVOPS_GROUP)
        assert st.st_uid == alice.pw_uid, (
            f"Directory '{ALICE_PROJECTS}' is not owned by user 'alice'."
        )
        assert st.st_gid == group.gr_gid, (
            f"Directory '{ALICE_PROJECTS}' is not group-owned by 'devops'."
        )
        mode = stat.S_IMODE(st.st_mode)
        assert mode == 0o770, (
            f"Directory '{ALICE_PROJECTS}' permissions are {oct(mode)}, expected 0o770 (drwxrwx---)."
        )

    def test_alice_security_notice(self):
        """The file /home/alice/security_notice.txt must exist, owned by alice:devops, permissions 600, correct content."""
        st = get_file_stat(ALICE_NOTICE)
        assert st is not None, f"File '{ALICE_NOTICE}' does not exist."

        alice = get_user(ALICE_USERNAME)
        group = get_group(DEVOPS_GROUP)
        assert st.st_uid == alice.pw_uid, (
            f"File '{ALICE_NOTICE}' is not owned by user 'alice'."
        )
        assert st.st_gid == group.gr_gid, (
            f"File '{ALICE_NOTICE}' is not group-owned by 'devops'."
        )
        mode = stat.S_IMODE(st.st_mode)
        assert mode == 0o600, (
            f"File '{ALICE_NOTICE}' permissions are {oct(mode)}, expected 0o600 (-rw-------)."
        )
        # Content check
        with open(ALICE_NOTICE, "r", encoding="utf-8") as f:
            content = f.read()
        assert content == SECURITY_NOTICE_CONTENT, (
            f"File '{ALICE_NOTICE}' content does not match the required notice.\n"
            f"Expected (repr): {repr(SECURITY_NOTICE_CONTENT)}\n"
            f"Found (repr):    {repr(content)}"
        )

    def test_hardening_log(self):
        """The file /home/user/hardening_log.txt must exist, owned by user:user, correct content, at least 644 perms."""
        st = get_file_stat(LOG_PATH)
        assert st is not None, f"File '{LOG_PATH}' does not exist."

        # Check ownership: must be user:user
        try:
            user = pwd.getpwnam("user")
            group = grp.getgrnam("user")
        except KeyError:
            pytest.skip("User 'user' or group 'user' does not exist on this system; skipping ownership check for log file.")
            user = None
            group = None

        if user and group:
            assert st.st_uid == user.pw_uid, (
                f"File '{LOG_PATH}' is not owned by user 'user'."
            )
            assert st.st_gid == group.gr_gid, (
                f"File '{LOG_PATH}' is not group-owned by 'user'."
            )

        mode = stat.S_IMODE(st.st_mode)
        assert mode & 0o644 == 0o644, (
            f"File '{LOG_PATH}' permissions are {oct(mode)}, must be at least 0o644 (-rw-r--r--)."
        )

        # Content check
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        assert content == HARDENING_LOG_CONTENT, (
            f"File '{LOG_PATH}' content does not match the required hardening log format.\n"
            f"Expected (repr): {repr(HARDENING_LOG_CONTENT)}\n"
            f"Found (repr):    {repr(content)}"
        )