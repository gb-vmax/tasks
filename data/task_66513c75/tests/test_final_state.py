# test_final_state.py

import os
import stat
import pytest

BASE_DIR = "/home/user/k8s-operator"

# Expected subdirectory permissions
EXPECTED_DIR_MODES = {
    "/home/user/k8s-operator/crds":   0o755,
    "/home/user/k8s-operator/rbac":   0o750,
    "/home/user/k8s-operator/deploy": 0o750,
}

# Expected file permissions and locations
EXPECTED_FILE_MODES = {
    "/home/user/k8s-operator/crds/cache-crd.yaml":          0o644,
    "/home/user/k8s-operator/crds/index-crd.yaml":          0o644,
    "/home/user/k8s-operator/rbac/operator-role.yaml":      0o640,
    "/home/user/k8s-operator/rbac/operator-rolebinding.yaml": 0o640,
    "/home/user/k8s-operator/deploy/operator-deploy.yaml":  0o640,
    "/home/user/k8s-operator/deploy/operator-svc.yaml":     0o640,
}

# Original files that must no longer exist at the root
ORIGINAL_ROOT_FILES = [
    "/home/user/k8s-operator/cache-crd.yaml",
    "/home/user/k8s-operator/index-crd.yaml",
    "/home/user/k8s-operator/operator-role.yaml",
    "/home/user/k8s-operator/operator-rolebinding.yaml",
    "/home/user/k8s-operator/operator-deploy.yaml",
    "/home/user/k8s-operator/operator-svc.yaml",
]

PERMISSIONS_TXT = "/home/user/k8s-operator/permissions.txt"

EXPECTED_PERMISSIONS_TXT = (
    "drwxr-xr-x /home/user/k8s-operator/crds\n"
    "-rw-r--r-- /home/user/k8s-operator/crds/cache-crd.yaml\n"
    "-rw-r--r-- /home/user/k8s-operator/crds/index-crd.yaml\n"
    "drwxr-x--- /home/user/k8s-operator/deploy\n"
    "-rw-r----- /home/user/k8s-operator/deploy/operator-deploy.yaml\n"
    "-rw-r----- /home/user/k8s-operator/deploy/operator-svc.yaml\n"
    "drwxr-x--- /home/user/k8s-operator/rbac\n"
    "-rw-r----- /home/user/k8s-operator/rbac/operator-role.yaml\n"
    "-rw-r----- /home/user/k8s-operator/rbac/operator-rolebinding.yaml\n"
)


def get_mode(path):
    """Return the permission bits (masked to 12 bits) for the given path."""
    return stat.S_IMODE(os.stat(path).st_mode)


def mode_to_symbolic(path):
    """Return a 10-character symbolic permission string for the given path."""
    st = os.stat(path)
    mode = st.st_mode
    return stat.filemode(mode)


# ── Subdirectory existence ──────────────────────────────────────────────────

class TestSubdirectoriesExist:
    @pytest.mark.parametrize("dirpath", list(EXPECTED_DIR_MODES.keys()))
    def test_subdirectory_exists(self, dirpath):
        assert os.path.isdir(dirpath), (
            f"Subdirectory '{dirpath}' does not exist. "
            "It should have been created by the agent."
        )

    @pytest.mark.parametrize("dirpath", list(EXPECTED_DIR_MODES.keys()))
    def test_subdirectory_is_not_symlink(self, dirpath):
        if os.path.exists(dirpath):
            assert not os.path.islink(dirpath), (
                f"'{dirpath}' is a symlink, expected a real directory."
            )


# ── Subdirectory permissions ────────────────────────────────────────────────

class TestSubdirectoryPermissions:
    @pytest.mark.parametrize("dirpath,expected_mode", list(EXPECTED_DIR_MODES.items()))
    def test_directory_permission(self, dirpath, expected_mode):
        assert os.path.isdir(dirpath), (
            f"Cannot check permissions: '{dirpath}' does not exist."
        )
        actual_mode = get_mode(dirpath)
        assert actual_mode == expected_mode, (
            f"Directory '{dirpath}' has wrong permissions.\n"
            f"Expected: {oct(expected_mode)} ({stat.filemode(stat.S_IFDIR | expected_mode)})\n"
            f"Actual:   {oct(actual_mode)} ({mode_to_symbolic(dirpath)})"
        )


# ── File existence ──────────────────────────────────────────────────────────

class TestFilesExistInSubdirectories:
    @pytest.mark.parametrize("filepath", list(EXPECTED_FILE_MODES.keys()))
    def test_file_exists(self, filepath):
        assert os.path.isfile(filepath), (
            f"File '{filepath}' does not exist. "
            "It should have been moved there by the agent."
        )

    @pytest.mark.parametrize("filepath", list(EXPECTED_FILE_MODES.keys()))
    def test_file_is_not_symlink(self, filepath):
        if os.path.exists(filepath):
            assert not os.path.islink(filepath), (
                f"'{filepath}' is a symlink, expected a regular file."
            )


# ── File permissions ────────────────────────────────────────────────────────

class TestFilePermissions:
    @pytest.mark.parametrize("filepath,expected_mode", list(EXPECTED_FILE_MODES.items()))
    def test_file_permission(self, filepath, expected_mode):
        assert os.path.isfile(filepath), (
            f"Cannot check permissions: '{filepath}' does not exist."
        )
        actual_mode = get_mode(filepath)
        assert actual_mode == expected_mode, (
            f"File '{filepath}' has wrong permissions.\n"
            f"Expected: {oct(expected_mode)} ({stat.filemode(stat.S_IFREG | expected_mode)})\n"
            f"Actual:   {oct(actual_mode)} ({mode_to_symbolic(filepath)})"
        )


# ── Original root files removed ─────────────────────────────────────────────

class TestOriginalFilesRemoved:
    @pytest.mark.parametrize("filepath", ORIGINAL_ROOT_FILES)
    def test_original_file_not_at_root(self, filepath):
        assert not os.path.exists(filepath), (
            f"File '{filepath}' still exists at the root of '{BASE_DIR}'. "
            "It should have been moved to the appropriate subdirectory."
        )


# ── permissions.txt existence and content ───────────────────────────────────

class TestPermissionsTxt:
    def test_permissions_txt_exists(self):
        assert os.path.isfile(PERMISSIONS_TXT), (
            f"File '{PERMISSIONS_TXT}' does not exist. "
            "The agent should have created this file."
        )

    def test_permissions_txt_is_not_symlink(self):
        if os.path.exists(PERMISSIONS_TXT):
            assert not os.path.islink(PERMISSIONS_TXT), (
                f"'{PERMISSIONS_TXT}' is a symlink, expected a regular file."
            )

    def test_permissions_txt_line_count(self):
        assert os.path.isfile(PERMISSIONS_TXT), (
            f"Cannot check line count: '{PERMISSIONS_TXT}' does not exist."
        )
        with open(PERMISSIONS_TXT, "r") as f:
            content = f.read()
        lines = content.splitlines()
        assert len(lines) == 9, (
            f"'{PERMISSIONS_TXT}' should have exactly 9 lines, "
            f"but has {len(lines)} lines.\n"
            f"Actual content:\n{content!r}"
        )

    def test_permissions_txt_ends_with_newline(self):
        assert os.path.isfile(PERMISSIONS_TXT), (
            f"Cannot check content: '{PERMISSIONS_TXT}' does not exist."
        )
        with open(PERMISSIONS_TXT, "r") as f:
            content = f.read()
        assert content.endswith("\n"), (
            f"'{PERMISSIONS_TXT}' should end with a newline character, but it does not.\n"
            f"Actual content:\n{content!r}"
        )

    def test_permissions_txt_exact_content(self):
        assert os.path.isfile(PERMISSIONS_TXT), (
            f"Cannot check content: '{PERMISSIONS_TXT}' does not exist."
        )
        with open(PERMISSIONS_TXT, "r") as f:
            actual_content = f.read()
        assert actual_content == EXPECTED_PERMISSIONS_TXT, (
            f"'{PERMISSIONS_TXT}' has unexpected content.\n"
            f"Expected:\n{EXPECTED_PERMISSIONS_TXT!r}\n"
            f"Actual:\n{actual_content!r}"
        )

    def test_permissions_txt_no_trailing_spaces(self):
        assert os.path.isfile(PERMISSIONS_TXT), (
            f"Cannot check content: '{PERMISSIONS_TXT}' does not exist."
        )
        with open(PERMISSIONS_TXT, "r") as f:
            lines = f.readlines()
        for i, line in enumerate(lines, start=1):
            stripped = line.rstrip("\n")
            assert stripped == stripped.rstrip(), (
                f"Line {i} in '{PERMISSIONS_TXT}' has trailing whitespace: {line!r}"
            )

    def test_permissions_txt_lines_sorted_alphabetically(self):
        assert os.path.isfile(PERMISSIONS_TXT), (
            f"Cannot check content: '{PERMISSIONS_TXT}' does not exist."
        )
        with open(PERMISSIONS_TXT, "r") as f:
            content = f.read()
        lines = content.splitlines()
        # Extract paths (second field) for sorting check
        paths = [line.split(" ", 1)[1] for line in lines if " " in line]
        assert paths == sorted(paths), (
            f"Lines in '{PERMISSIONS_TXT}' are not sorted alphabetically by path.\n"
            f"Actual paths:\n" + "\n".join(paths)
        )

    def test_permissions_txt_each_line_format(self):
        """Each line must be: 10-char permission string, single space, absolute path."""
        assert os.path.isfile(PERMISSIONS_TXT), (
            f"Cannot check content: '{PERMISSIONS_TXT}' does not exist."
        )
        with open(PERMISSIONS_TXT, "r") as f:
            lines = f.read().splitlines()
        for i, line in enumerate(lines, start=1):
            parts = line.split(" ", 1)
            assert len(parts) == 2, (
                f"Line {i} in '{PERMISSIONS_TXT}' does not have the expected format "
                f"'<perms> <path>': {line!r}"
            )
            perms, path = parts
            assert len(perms) == 10, (
                f"Line {i} in '{PERMISSIONS_TXT}': permission string '{perms}' "
                f"should be exactly 10 characters, got {len(perms)}."
            )
            assert path.startswith("/"), (
                f"Line {i} in '{PERMISSIONS_TXT}': path '{path}' "
                "should be an absolute path."
            )


# ── Base directory still intact ─────────────────────────────────────────────

class TestBaseDirectory:
    def test_base_directory_exists(self):
        assert os.path.isdir(BASE_DIR), (
            f"Base directory '{BASE_DIR}' does not exist."
        )

    def test_base_directory_is_not_symlink(self):
        assert not os.path.islink(BASE_DIR), (
            f"Base directory '{BASE_DIR}' is a symlink, expected a real directory."
        )