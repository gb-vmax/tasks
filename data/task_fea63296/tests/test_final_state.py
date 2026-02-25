# test_final_state.py

import os
import pwd
import stat
import pytest

HOME = '/home/user'
BUILD_ARTIFACTS = os.path.join(HOME, 'build_artifacts')
ANDROID_DIR = os.path.join(BUILD_ARTIFACTS, 'android')
IOS_DIR = os.path.join(BUILD_ARTIFACTS, 'ios')
REPORT_LOG = os.path.join(BUILD_ARTIFACTS, 'artifact_report.log')

ANDROID_FILES = [
    ('app-release.apk', 997),
    ('proguard-rules.txt', 415),
]
IOS_FILES = [
    ('Runner.app', 2234),
    ('launch.log', 78),
]

ANDROID_OLD_PATH = os.path.join(HOME, 'android_old')
IOS_OLD_PATH = os.path.join(HOME, 'some/other/path/ios_old')

def get_owner(path):
    return pwd.getpwuid(os.stat(path).st_uid).pw_name

def check_permissions(path, expected_mode):
    st = os.stat(path)
    return stat.S_IMODE(st.st_mode) == expected_mode

def read_file_bytes(path):
    with open(path, 'rb') as f:
        return f.read()

def list_files_recursive(directory):
    """List all files (not directories) recursively, with absolute paths."""
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for fname in files:
            file_paths.append(os.path.join(root, fname))
    return file_paths

@pytest.mark.describe("Final filesystem state after student action")
class TestFinalState:
    def test_build_artifacts_dirs_exist_and_permissions(self):
        for d in [BUILD_ARTIFACTS, ANDROID_DIR, IOS_DIR]:
            assert os.path.isdir(d), f"Directory {d} does not exist. It must be created."
            owner = get_owner(d)
            assert owner == 'user', f"Directory {d} must be owned by 'user', but owner is '{owner}'."
            assert check_permissions(d, 0o700), f"Directory {d} must have permissions 700, but has {oct(stat.S_IMODE(os.stat(d).st_mode))}."

    @pytest.mark.parametrize("fname,expected_size", ANDROID_FILES)
    def test_android_artifacts_exist_and_content_permissions(self, fname, expected_size):
        dest = os.path.join(ANDROID_DIR, fname)
        assert os.path.isfile(dest), f"Expected file {dest} does not exist in android artifacts."
        # Check permissions
        assert check_permissions(dest, 0o600), f"File {dest} must have permissions 600, but has {oct(stat.S_IMODE(os.stat(dest).st_mode))}."
        # Check ownership
        owner = get_owner(dest)
        assert owner == 'user', f"File {dest} must be owned by 'user', but is owned by '{owner}'."
        # Check content size
        actual_size = os.path.getsize(dest)
        assert actual_size == expected_size, f"File {dest} should have size {expected_size} bytes, found {actual_size}."

    @pytest.mark.parametrize("fname,expected_size", IOS_FILES)
    def test_ios_artifacts_exist_and_content_permissions(self, fname, expected_size):
        dest = os.path.join(IOS_DIR, fname)
        assert os.path.isfile(dest), f"Expected file {dest} does not exist in ios artifacts."
        # Check permissions
        assert check_permissions(dest, 0o600), f"File {dest} must have permissions 600, but has {oct(stat.S_IMODE(os.stat(dest).st_mode))}."
        # Check ownership
        owner = get_owner(dest)
        assert owner == 'user', f"File {dest} must be owned by 'user', but is owned by '{owner}'."
        # Check content size
        actual_size = os.path.getsize(dest)
        assert actual_size == expected_size, f"File {dest} should have size {expected_size} bytes, found {actual_size}."

    def test_android_old_and_ios_old_deleted(self):
        assert not os.path.exists(ANDROID_OLD_PATH), f"Directory {ANDROID_OLD_PATH} must be removed after migration."
        assert not os.path.exists(IOS_OLD_PATH), f"Directory {IOS_OLD_PATH} must be removed after migration."

    def test_no_android_old_or_ios_old_anywhere_under_home(self):
        # Walk entire /home/user and ensure no dir named android_old or ios_old exists
        for root, dirs, files in os.walk(HOME):
            for d in dirs:
                assert d not in ('android_old', 'ios_old'), (
                    f"Found leftover directory '{d}' in {os.path.join(root, d)}. "
                    "All android_old and ios_old directories must be removed after migration."
                )

    def test_no_extra_files_or_dirs_in_build_artifacts(self):
        # build_artifacts must contain only: android/, ios/, artifact_report.log
        contents = set(os.listdir(BUILD_ARTIFACTS))
        expected = {'android', 'ios', 'artifact_report.log'}
        extra = contents - expected
        missing = expected - contents
        assert not missing, f"Missing expected entries in {BUILD_ARTIFACTS}: {missing}."
        assert not extra, f"Unexpected extra entries in {BUILD_ARTIFACTS}: {extra}."

    def test_no_extra_files_in_android(self):
        files = os.listdir(ANDROID_DIR)
        expected = set(f for f, _ in ANDROID_FILES)
        actual = set(files)
        extra = actual - expected
        missing = expected - actual
        assert not missing, f"Missing expected files in {ANDROID_DIR}: {missing}."
        assert not extra, f"Unexpected extra files in {ANDROID_DIR}: {extra}."

    def test_no_extra_files_in_ios(self):
        files = os.listdir(IOS_DIR)
        expected = set(f for f, _ in IOS_FILES)
        actual = set(files)
        extra = actual - expected
        missing = expected - actual
        assert not missing, f"Missing expected files in {IOS_DIR}: {missing}."
        assert not extra, f"Unexpected extra files in {IOS_DIR}: {extra}."

    def test_artifact_report_log_exists_and_permissions(self):
        assert os.path.isfile(REPORT_LOG), f"Report log {REPORT_LOG} does not exist."
        assert check_permissions(REPORT_LOG, 0o600), f"Report log {REPORT_LOG} must have permissions 600."
        owner = get_owner(REPORT_LOG)
        assert owner == 'user', f"Report log {REPORT_LOG} must be owned by 'user', but is owned by '{owner}'."

    def test_artifact_report_log_contents(self):
        # Construct expected lines
        android_files = [os.path.join(ANDROID_DIR, f) for f, _ in ANDROID_FILES]
        ios_files = [os.path.join(IOS_DIR, f) for f, _ in IOS_FILES]
        expected_lines = sorted(android_files + ios_files)
        expected_lines.append(f"Android files: {len(ANDROID_FILES)}")
        expected_lines.append(f"iOS files: {len(IOS_FILES)}")

        with open(REPORT_LOG, 'rt', encoding='utf-8') as f:
            lines = [line.rstrip('\n') for line in f]

        assert lines == expected_lines, (
            f"artifact_report.log contents do not match expected format.\n"
            f"Expected lines:\n{expected_lines}\n"
            f"Actual lines:\n{lines}\n"
            "Make sure the log contains absolute file paths for every file (not directories), "
            "sorted alphabetically, one per line, followed by the Android/iOS file counts."
        )

    def test_artifact_report_log_lists_only_actual_files(self):
        # Ensure the report only lists files that actually exist under android/ and ios/
        with open(REPORT_LOG, 'rt', encoding='utf-8') as f:
            lines = [line.rstrip('\n') for line in f]
        # Remove the last two lines (counts)
        file_lines = lines[:-2]
        for fpath in file_lines:
            assert os.path.isfile(fpath), (
                f"File path '{fpath}' listed in artifact_report.log does not exist or is not a file."
            )

    def test_artifact_report_log_counts_match_actual_files(self):
        # Checks that the Android/iOS file counts in report match the actual files
        with open(REPORT_LOG, 'rt', encoding='utf-8') as f:
            lines = [line.rstrip('\n') for line in f]
        android_count = sum(1 for l in lines if l.startswith(ANDROID_DIR + os.sep))
        ios_count = sum(1 for l in lines if l.startswith(IOS_DIR + os.sep))
        assert lines[-2] == f"Android files: {android_count}", (
            f"Android files count line in report log is incorrect: got '{lines[-2]}', expected 'Android files: {android_count}'"
        )
        assert lines[-1] == f"iOS files: {ios_count}", (
            f"iOS files count line in report log is incorrect: got '{lines[-1]}', expected 'iOS files: {ios_count}'"
        )