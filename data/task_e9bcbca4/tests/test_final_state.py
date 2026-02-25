# test_final_state.py

import os
import pytest

DASHBOARDS_DIR = '/home/user/dashboards'
PROD_DASHBOARD = '/home/user/dashboards/prod_dashboard.json'
STAGING_DASHBOARD = '/home/user/dashboards/staging_dashboard.json'

ACTIVE_SYMLINK = '/home/user/active_dashboard.json'
ENVS_PROD_DIR = '/home/user/envs/prod'
ENVS_STAGING_DIR = '/home/user/envs/staging'

ENVS_PROD_DASHBOARD_LINK = '/home/user/envs/prod/dashboard.json'
ENVS_STAGING_DASHBOARD_LINK = '/home/user/envs/staging/dashboard.json'

DASHBOARD_SYMLINK_LOG = '/home/user/dashboard_symlink_check.log'

EXPECTED_LOG_LINES = [
    f"{ACTIVE_SYMLINK}\t{PROD_DASHBOARD}",
    f"{ENVS_PROD_DASHBOARD_LINK}\t{PROD_DASHBOARD}",
    f"{ENVS_STAGING_DASHBOARD_LINK}\t{STAGING_DASHBOARD}",
]

@pytest.mark.describe("Final state of dashboards symlinks and verification log after task completion")
class TestFinalState:
    def test_active_dashboard_symlink_points_to_prod(self):
        assert os.path.islink(ACTIVE_SYMLINK), (
            f"{ACTIVE_SYMLINK} is not a symbolic link. "
            "It must be a symlink pointing to /home/user/dashboards/prod_dashboard.json."
        )
        target = os.readlink(ACTIVE_SYMLINK)
        abs_target = (
            target if os.path.isabs(target)
            else os.path.abspath(os.path.join(os.path.dirname(ACTIVE_SYMLINK), target))
        )
        assert abs_target == PROD_DASHBOARD, (
            f"{ACTIVE_SYMLINK} points to {abs_target!r}, "
            f"but should point to {PROD_DASHBOARD!r}."
        )

    def test_envs_prod_dashboard_symlink_points_to_prod(self):
        assert os.path.islink(ENVS_PROD_DASHBOARD_LINK), (
            f"{ENVS_PROD_DASHBOARD_LINK} is not a symbolic link. "
            "It must be a symlink pointing to /home/user/dashboards/prod_dashboard.json."
        )
        target = os.readlink(ENVS_PROD_DASHBOARD_LINK)
        abs_target = (
            target if os.path.isabs(target)
            else os.path.abspath(os.path.join(os.path.dirname(ENVS_PROD_DASHBOARD_LINK), target))
        )
        assert abs_target == PROD_DASHBOARD, (
            f"{ENVS_PROD_DASHBOARD_LINK} points to {abs_target!r}, "
            f"but should point to {PROD_DASHBOARD!r}."
        )

    def test_envs_staging_dashboard_symlink_points_to_staging(self):
        assert os.path.islink(ENVS_STAGING_DASHBOARD_LINK), (
            f"{ENVS_STAGING_DASHBOARD_LINK} is not a symbolic link. "
            "It must be a symlink pointing to /home/user/dashboards/staging_dashboard.json."
        )
        target = os.readlink(ENVS_STAGING_DASHBOARD_LINK)
        abs_target = (
            target if os.path.isabs(target)
            else os.path.abspath(os.path.join(os.path.dirname(ENVS_STAGING_DASHBOARD_LINK), target))
        )
        assert abs_target == STAGING_DASHBOARD, (
            f"{ENVS_STAGING_DASHBOARD_LINK} points to {abs_target!r}, "
            f"but should point to {STAGING_DASHBOARD!r}."
        )

    def test_dashboard_symlink_check_log_exists_and_correct(self):
        assert os.path.isfile(DASHBOARD_SYMLINK_LOG), (
            f"Verification log file missing: {DASHBOARD_SYMLINK_LOG}"
        )
        with open(DASHBOARD_SYMLINK_LOG, 'r', encoding='utf-8') as f:
            lines = [line.rstrip('\n') for line in f]
        # Check number of lines first
        if len(lines) != 3:
            pytest.fail(
                f"Log file {DASHBOARD_SYMLINK_LOG} should contain exactly 3 lines, found {len(lines)}.\n"
                f"Actual content:\n{lines}"
            )
        # Check each line's tab separation and content
        for i, (line, expected) in enumerate(zip(lines, EXPECTED_LOG_LINES), 1):
            if line != expected:
                pytest.fail(
                    f"Log file {DASHBOARD_SYMLINK_LOG}, line {i} does not match expected.\n"
                    f"Expected: {expected!r}\n"
                    f"Found:    {line!r}\n"
                    "Each line must contain absolute symlink path, a TAB, and its absolute target."
                )
        # Check for tab separation, not spaces or other whitespace
        for i, line in enumerate(lines, 1):
            fields = line.split('\t')
            if len(fields) != 2:
                pytest.fail(
                    f"Log file {DASHBOARD_SYMLINK_LOG}, line {i} does not have exactly one TAB character. "
                    f"Line: {line!r}"
                )
            if ' ' in line.replace('\t', ''):
                # Allow spaces in filenames, but not as separator
                pass  # Do not check for spaces unless it's in place of TAB

    def test_dashboard_symlink_targets_match_log(self):
        # Cross-check: for each log entry, the symlink and its target must match in the filesystem
        with open(DASHBOARD_SYMLINK_LOG, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.rstrip('\n')
                if not line:
                    continue  # skip blank (shouldn't happen)
                symlink_path, expected_target = line.split('\t')
                assert os.path.islink(symlink_path), (
                    f"Symlink listed in log does not exist or is not a symlink: {symlink_path}"
                )
                actual_target = os.readlink(symlink_path)
                actual_abs_target = (
                    actual_target if os.path.isabs(actual_target)
                    else os.path.abspath(os.path.join(os.path.dirname(symlink_path), actual_target))
                )
                assert actual_abs_target == expected_target, (
                    f"Symlink {symlink_path} points to {actual_abs_target!r}, "
                    f"but log says it should point to {expected_target!r}."
                )