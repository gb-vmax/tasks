# test_final_state.py

"""
Pytest suite to validate the final state of /home/user/db_query_optim after the query optimization task.

Checks:
- /home/user/db_query_optim/old_links exists and is a directory.
- If /home/user/db_query_optim/active_query.sql existed as a symlink before, it has been moved to old_links/.
- The three new symlinks exist in /home/user/db_query_optim and point to the correct absolute .sql files.
- /home/user/db_query_optim/symlink_report.txt exists and has exactly the required three lines, in order, no more, no less.
"""

import os
import pytest

DB_DIR = "/home/user/db_query_optim"
PROD_SQL = os.path.join(DB_DIR, "query_prod.sql")
TEST_SQL = os.path.join(DB_DIR, "query_test.sql")
DEV_SQL = os.path.join(DB_DIR, "query_dev.sql")

SYMLINKS = [
    ("active_query_prod.sql", PROD_SQL),
    ("active_query_test.sql", TEST_SQL),
    ("active_query_dev.sql", DEV_SQL),
]

OLD_LINKS_DIR = os.path.join(DB_DIR, "old_links")
ACTIVE_SYMLINK = os.path.join(DB_DIR, "active_query.sql")
SYMLINK_REPORT = os.path.join(DB_DIR, "symlink_report.txt")

@pytest.mark.describe("Final OS/filesystem state after optimization task")
class TestFinalState:

    def test_old_links_directory_exists(self):
        assert os.path.isdir(OLD_LINKS_DIR), (
            f"Directory '{OLD_LINKS_DIR}' does not exist. "
            "It must be created to store old symlinks."
        )

    def test_active_query_symlink_moved_if_it_existed(self):
        """
        If active_query.sql existed as a symlink before, it must now be in old_links/.
        If it did not exist or was not a symlink, nothing should be moved.
        We check for the presence of old_links/active_query.sql if it was moved.
        """
        old_link = os.path.join(OLD_LINKS_DIR, "active_query.sql")
        # If old_links/active_query.sql exists, it must be a symlink and point to a valid .sql file
        if os.path.islink(old_link):
            target = os.readlink(old_link)
            # Accept both relative and absolute links, but must resolve to one of the three allowed files
            abs_target = (
                os.path.abspath(os.path.join(OLD_LINKS_DIR, target))
                if not os.path.isabs(target)
                else target
            )
            allowed_targets = {PROD_SQL, TEST_SQL, DEV_SQL}
            assert abs_target in allowed_targets, (
                f"Symlink '{old_link}' points to '{target}', "
                f"which does not resolve to one of the allowed SQL template files:\n"
                f"- {PROD_SQL}\n- {TEST_SQL}\n- {DEV_SQL}"
            )
            # It should no longer be present in the main directory
            assert not os.path.exists(ACTIVE_SYMLINK), (
                f"Symlink '{ACTIVE_SYMLINK}' should have been moved to '{old_link}', "
                "but it still exists in the main directory."
            )
        else:
            # If old_links/active_query.sql does not exist,
            # then there must be no active_query.sql symlink in the main directory either.
            if os.path.exists(ACTIVE_SYMLINK):
                assert not os.path.islink(ACTIVE_SYMLINK), (
                    f"'{ACTIVE_SYMLINK}' is still a symlink, it should have been moved to '{old_link}'."
                )

    @pytest.mark.parametrize("symlink_name,target_path", SYMLINKS)
    def test_new_symlinks_exist_and_point_correctly(self, symlink_name, target_path):
        symlink_path = os.path.join(DB_DIR, symlink_name)
        assert os.path.islink(symlink_path), (
            f"Symlink '{symlink_path}' does not exist or is not a symlink. "
            f"Create this symlink to point to '{target_path}'."
        )
        link_target = os.readlink(symlink_path)
        # Accept both relative and absolute links, but must resolve to the exact absolute path
        resolved_target = (
            os.path.abspath(os.path.join(DB_DIR, link_target))
            if not os.path.isabs(link_target)
            else link_target
        )
        assert resolved_target == target_path, (
            f"Symlink '{symlink_path}' points to '{link_target}' "
            f"(resolves to '{resolved_target}'), but it must point to '{target_path}'."
        )

    def test_symlink_report_txt_content_and_format(self):
        assert os.path.isfile(SYMLINK_REPORT), (
            f"Report file '{SYMLINK_REPORT}' does not exist. "
            "You must create this report as specified."
        )
        with open(SYMLINK_REPORT, "r") as f:
            lines = [line.rstrip('\n') for line in f.readlines()]
        expected_lines = [
            f"{symlink} -> {target}"
            for symlink, target in SYMLINKS
        ]
        assert lines == expected_lines, (
            f"Report file '{SYMLINK_REPORT}' does not have the correct content.\n"
            f"Expected lines:\n" +
            "\n".join(repr(l) for l in expected_lines) +
            "\nActual lines:\n" +
            "\n".join(repr(l) for l in lines)
        )

    def test_only_expected_symlinks_exist_in_db_query_optim(self):
        """
        Ensure that only the three new symlinks exist in DB_DIR,
        and that active_query.sql is NOT present as a symlink.
        """
        found_symlinks = []
        for entry in os.listdir(DB_DIR):
            entry_path = os.path.join(DB_DIR, entry)
            if os.path.islink(entry_path):
                found_symlinks.append(entry)
        expected_symlinks = {name for name, _ in SYMLINKS}
        unexpected_symlinks = set(found_symlinks) - expected_symlinks
        missing_symlinks = expected_symlinks - set(found_symlinks)
        assert not missing_symlinks, (
            f"The following expected symlinks are missing in '{DB_DIR}': {sorted(missing_symlinks)}"
        )
        assert not unexpected_symlinks, (
            f"The following unexpected symlinks are present in '{DB_DIR}': {sorted(unexpected_symlinks)}"
        )
        # Ensure active_query.sql is not a symlink in DB_DIR
        active_symlink_path = os.path.join(DB_DIR, "active_query.sql")
        assert not os.path.islink(active_symlink_path), (
            f"Symlink '{active_symlink_path}' should have been moved to '{OLD_LINKS_DIR}', "
            "but it still exists in the main directory."
        )