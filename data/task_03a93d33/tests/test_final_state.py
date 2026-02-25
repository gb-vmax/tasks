# test_final_state.py

import os
import pytest

BUILD_OUTPUT = '/home/user/build_output'
OBJ_ARCHIVE = os.path.join(BUILD_OUTPUT, 'obj_archive')
V4_DIR = os.path.join(BUILD_OUTPUT, 'v4')
MOVE_LOG = os.path.join(OBJ_ARCHIVE, 'move-log.txt')

# The expected .o files that should have been moved (original -> new locations)
EXPECTED_MOVES = [
    (os.path.join(BUILD_OUTPUT, 'main.o'), os.path.join(OBJ_ARCHIVE, 'main.o')),
    (os.path.join(BUILD_OUTPUT, 'utils.o'), os.path.join(OBJ_ARCHIVE, 'utils.o')),
    (os.path.join(V4_DIR, 'math.o'), os.path.join(OBJ_ARCHIVE, 'v4', 'math.o')),
    (os.path.join(V4_DIR, 'parse.o'), os.path.join(OBJ_ARCHIVE, 'v4', 'parse.o')),
]
EXPECTED_MOVE_LOG_LINES = [
    f"{src} -> {dst}" for src, dst in EXPECTED_MOVES
]

# All other files that must NOT be moved or altered
EXPECTED_REMAINING_FILES = {
    os.path.join(BUILD_OUTPUT, 'libmath.a'),
    os.path.join(BUILD_OUTPUT, 'build.log'),
    os.path.join(BUILD_OUTPUT, 'results.tmp'),
    os.path.join(BUILD_OUTPUT, 'readme.txt'),
    os.path.join(V4_DIR, 'datagen.tmp'),
    os.path.join(V4_DIR, 'test.tar.gz'),
}

@pytest.mark.describe("Final filesystem state after organizing .o build artifacts")
class TestFinalState:

    @pytest.mark.it("obj_archive directory exists after the task")
    def test_obj_archive_dir_exists(self):
        assert os.path.isdir(OBJ_ARCHIVE), (
            f"Directory {OBJ_ARCHIVE} does not exist after the task. "
            "You must create it and move .o files into it."
        )

    @pytest.mark.it("obj_archive contains moved .o files in correct mirrored structure")
    def test_obj_archive_contains_moved_o_files(self):
        for src, dst in EXPECTED_MOVES:
            assert os.path.isfile(dst), (
                f"Expected .o file {dst} not found in obj_archive. "
                f"Did you move {src} to the correct location?"
            )

    @pytest.mark.it("original .o files are absent from their old locations")
    def test_original_o_files_absent(self):
        for src, dst in EXPECTED_MOVES:
            assert not os.path.exists(src), (
                f".o file {src} still exists in its original location. "
                "You must move, not copy, all .o files to obj_archive."
            )

    @pytest.mark.it("obj_archive contains mirrored v4 subdirectory for nested .o files")
    def test_obj_archive_v4_subdir(self):
        v4_subdir = os.path.join(OBJ_ARCHIVE, 'v4')
        assert os.path.isdir(v4_subdir), (
            f"Expected subdirectory {v4_subdir} in obj_archive for nested .o files."
        )

    @pytest.mark.it("obj_archive contains only the four .o files and move-log.txt (and v4/ subdir)")
    def test_obj_archive_has_no_extra_files(self):
        # Collect all files and dirs in obj_archive recursively
        found = set()
        for dirpath, dirnames, filenames in os.walk(OBJ_ARCHIVE):
            for fname in filenames:
                found.add(os.path.join(dirpath, fname))
        expected = {
            os.path.join(OBJ_ARCHIVE, 'main.o'),
            os.path.join(OBJ_ARCHIVE, 'utils.o'),
            os.path.join(OBJ_ARCHIVE, 'move-log.txt'),
            os.path.join(OBJ_ARCHIVE, 'v4', 'math.o'),
            os.path.join(OBJ_ARCHIVE, 'v4', 'parse.o'),
        }
        assert found == expected, (
            f"Unexpected files in {OBJ_ARCHIVE}.\n"
            f"Expected: {expected}\n"
            f"Found: {found}"
        )

    @pytest.mark.it("move-log.txt exists and lists all move operations in correct format")
    def test_move_log_file_exists_and_content(self):
        assert os.path.isfile(MOVE_LOG), (
            f"{MOVE_LOG} does not exist after the task. "
            "You must create it with the correct move operations."
        )
        with open(MOVE_LOG, 'r', encoding='utf-8') as f:
            lines = [line.rstrip('\n') for line in f]
        # The order may vary, but all four lines must be present and no more.
        missing = set(EXPECTED_MOVE_LOG_LINES) - set(lines)
        extra = set(lines) - set(EXPECTED_MOVE_LOG_LINES)
        assert not missing, (
            f"move-log.txt is missing the following move entries:\n{missing}\n"
            f"Actual lines: {lines}"
        )
        assert not extra, (
            f"move-log.txt contains unexpected lines:\n{extra}\n"
            f"Expected lines: {EXPECTED_MOVE_LOG_LINES}"
        )
        assert len(lines) == 4, (
            f"move-log.txt must contain exactly 4 lines, one for each .o file. "
            f"Found {len(lines)} lines."
        )

    @pytest.mark.it("non-.o files remain untouched in their original locations")
    def test_non_o_files_untouched(self):
        for path in EXPECTED_REMAINING_FILES:
            assert os.path.isfile(path), (
                f"Non-.o file {path} is missing or was moved/altered. "
                "Only .o files should have been moved."
            )

    @pytest.mark.it("non-.o files in build_output and v4 are not duplicated in obj_archive")
    def test_no_non_o_files_in_obj_archive(self):
        # Walk obj_archive and check for unexpected file extensions
        for dirpath, dirnames, filenames in os.walk(OBJ_ARCHIVE):
            for fname in filenames:
                if fname == 'move-log.txt':
                    continue
                if not fname.endswith('.o'):
                    assert False, (
                        f"Unexpected non-.o file {os.path.join(dirpath, fname)} found in obj_archive. "
                        "Only .o files and move-log.txt should be present."
                    )

    @pytest.mark.it("no unexpected files or directories in build_output")
    def test_no_extra_files_dirs_in_build_output(self):
        expected_files = {
            "libmath.a",
            "build.log",
            "results.tmp",
            "readme.txt",
            "v4",
            "obj_archive",
        }
        actual = set(os.listdir(BUILD_OUTPUT))
        assert expected_files == actual, (
            f"Unexpected files or directories in {BUILD_OUTPUT}.\n"
            f"Expected: {expected_files}\n"
            f"Found: {actual}"
        )

    @pytest.mark.it("no unexpected files or directories in build_output/v4")
    def test_no_extra_files_dirs_in_v4(self):
        expected_files = {
            "datagen.tmp",
            "test.tar.gz",
        }
        actual = set(os.listdir(V4_DIR))
        assert expected_files == actual, (
            f"Unexpected files or directories in {V4_DIR} after .o files moved.\n"
            f"Expected: {expected_files}\n"
            f"Found: {actual}"
        )