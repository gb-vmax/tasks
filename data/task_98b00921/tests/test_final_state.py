# test_final_state.py

import os
import pytest

BASE = "/home/user/build_env"

def path(*parts):
    return os.path.join(BASE, *parts)


# ---------------------------------------------------------------------------
# 1. current-sdk symlink is fixed and relative
# ---------------------------------------------------------------------------

def test_current_sdk_is_symlink():
    p = path("sdks", "current-sdk")
    assert os.path.islink(p), (
        f"{p} must exist as a symbolic link, but it does not"
    )

def test_current_sdk_target_is_relative():
    p = path("sdks", "current-sdk")
    target = os.readlink(p)
    assert not os.path.isabs(target), (
        f"{p} must be a relative symlink, but its target is absolute: {target!r}"
    )

def test_current_sdk_target_value():
    p = path("sdks", "current-sdk")
    target = os.readlink(p)
    assert target == "android-34", (
        f"{p} must point to 'android-34', but points to {target!r}"
    )

def test_current_sdk_resolves():
    p = path("sdks", "current-sdk")
    assert os.path.exists(p), (
        f"{p} must resolve to an existing path (android-34), but it is broken"
    )


# ---------------------------------------------------------------------------
# 2. build-tools-active symlink is repointed and relative
# ---------------------------------------------------------------------------

def test_build_tools_active_is_symlink():
    p = path("tools", "build-tools-active")
    assert os.path.islink(p), (
        f"{p} must exist as a symbolic link, but it does not"
    )

def test_build_tools_active_target_is_relative():
    p = path("tools", "build-tools-active")
    target = os.readlink(p)
    assert not os.path.isabs(target), (
        f"{p} must be a relative symlink, but its target is absolute: {target!r}"
    )

def test_build_tools_active_target_value():
    p = path("tools", "build-tools-active")
    target = os.readlink(p)
    assert target == "build-tools-34.0.0", (
        f"{p} must point to 'build-tools-34.0.0', but points to {target!r}"
    )

def test_build_tools_active_resolves():
    p = path("tools", "build-tools-active")
    assert os.path.exists(p), (
        f"{p} must resolve to an existing path (build-tools-34.0.0), but it is broken"
    )


# ---------------------------------------------------------------------------
# 3. NDK symlinks exist
# ---------------------------------------------------------------------------

def test_ndk_current_is_symlink():
    p = path("ndk", "ndk-current")
    assert os.path.islink(p), (
        f"{p} must exist as a symbolic link, but it does not"
    )

def test_ndk_current_target_is_relative():
    p = path("ndk", "ndk-current")
    target = os.readlink(p)
    assert not os.path.isabs(target), (
        f"{p} must be a relative symlink, but its target is absolute: {target!r}"
    )

def test_ndk_current_target_value():
    p = path("ndk", "ndk-current")
    target = os.readlink(p)
    assert target == "ndk-r26b", (
        f"{p} must point to 'ndk-r26b', but points to {target!r}"
    )

def test_ndk_current_resolves():
    p = path("ndk", "ndk-current")
    assert os.path.exists(p), (
        f"{p} must resolve to an existing path (ndk-r26b), but it is broken"
    )

def test_ndk_active_is_symlink():
    p = path("tools", "ndk-active")
    assert os.path.islink(p), (
        f"{p} must exist as a symbolic link, but it does not"
    )

def test_ndk_active_target_is_absolute():
    p = path("tools", "ndk-active")
    target = os.readlink(p)
    assert os.path.isabs(target), (
        f"{p} must be an absolute symlink, but its target is relative: {target!r}"
    )

def test_ndk_active_target_value():
    p = path("tools", "ndk-active")
    target = os.readlink(p)
    expected = "/home/user/build_env/ndk/ndk-r26b"
    assert target == expected, (
        f"{p} must point to '{expected}', but points to {target!r}"
    )

def test_ndk_active_resolves():
    p = path("tools", "ndk-active")
    assert os.path.exists(p), (
        f"{p} must resolve to an existing path (/home/user/build_env/ndk/ndk-r26b), but it is broken"
    )


# ---------------------------------------------------------------------------
# 4. java-home symlink exists and is relative
# ---------------------------------------------------------------------------

def test_java_home_is_symlink():
    p = path("java", "java-home")
    assert os.path.islink(p), (
        f"{p} must exist as a symbolic link, but it does not"
    )

def test_java_home_target_is_relative():
    p = path("java", "java-home")
    target = os.readlink(p)
    assert not os.path.isabs(target), (
        f"{p} must be a relative symlink, but its target is absolute: {target!r}"
    )

def test_java_home_target_value():
    p = path("java", "java-home")
    target = os.readlink(p)
    assert target == "jdk-17.0.9", (
        f"{p} must point to 'jdk-17.0.9', but points to {target!r}"
    )

def test_java_home_resolves():
    p = path("java", "java-home")
    assert os.path.exists(p), (
        f"{p} must resolve to an existing path (jdk-17.0.9), but it is broken"
    )


# ---------------------------------------------------------------------------
# 5. symlink_manifest.txt correctness
# ---------------------------------------------------------------------------

MANIFEST = path("symlink_manifest.txt")

EXPECTED_MANIFEST = """\
/home/user/build_env/java/java-home -> jdk-17.0.9 [OK]
/home/user/build_env/ndk/ndk-current -> ndk-r26b [OK]
/home/user/build_env/sdks/current-sdk -> android-34 [OK]
/home/user/build_env/tools/build-tools-active -> build-tools-34.0.0 [OK]
/home/user/build_env/tools/ndk-active -> /home/user/build_env/ndk/ndk-r26b [OK]
"""

def test_manifest_exists():
    assert os.path.exists(MANIFEST), (
        f"{MANIFEST} must exist as a regular file, but it does not"
    )

def test_manifest_is_regular_file_not_symlink():
    assert not os.path.islink(MANIFEST), (
        f"{MANIFEST} must be a regular file, not a symbolic link"
    )
    assert os.path.isfile(MANIFEST), (
        f"{MANIFEST} must be a regular file"
    )

def test_manifest_line_count():
    with open(MANIFEST, "r") as f:
        content = f.read()
    lines = content.splitlines()
    assert len(lines) == 5, (
        f"{MANIFEST} must have exactly 5 lines, but has {len(lines)} lines.\n"
        f"Actual content:\n{content!r}"
    )

def test_manifest_ends_with_newline():
    with open(MANIFEST, "rb") as f:
        content = f.read()
    assert content.endswith(b"\n"), (
        f"{MANIFEST} must end with a newline character, but it does not"
    )

def test_manifest_no_trailing_spaces():
    with open(MANIFEST, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, 1):
        stripped = line.rstrip("\n")
        assert stripped == stripped.rstrip(), (
            f"{MANIFEST} line {i} has trailing spaces: {line!r}"
        )

def test_manifest_exact_content():
    with open(MANIFEST, "r") as f:
        actual = f.read()
    assert actual == EXPECTED_MANIFEST, (
        f"{MANIFEST} content does not match expected.\n"
        f"Expected:\n{EXPECTED_MANIFEST!r}\n"
        f"Actual:\n{actual!r}"
    )

def test_manifest_is_sorted_alphabetically():
    with open(MANIFEST, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    paths = [line.split(" -> ")[0] for line in lines]
    assert paths == sorted(paths), (
        f"{MANIFEST} lines are not sorted alphabetically by symlink path.\n"
        f"Actual order: {paths}"
    )

def test_manifest_does_not_include_itself():
    with open(MANIFEST, "r") as f:
        content = f.read()
    assert MANIFEST not in content, (
        f"{MANIFEST} must not appear in the manifest (it is not a symlink)"
    )

def test_manifest_each_line_format():
    """Each line must match: <path> -> <target> [OK|BROKEN]"""
    import re
    pattern = re.compile(r'^/.+ -> .+ \[(OK|BROKEN)\]$')
    with open(MANIFEST, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    for line in lines:
        assert pattern.match(line), (
            f"Line in {MANIFEST} does not match expected format '<path> -> <target> [OK|BROKEN]':\n"
            f"  Got: {line!r}"
        )

def test_manifest_all_statuses_are_ok():
    with open(MANIFEST, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    for line in lines:
        assert line.endswith("[OK]"), (
            f"All symlinks in the manifest should have status [OK], but found: {line!r}"
        )

def test_manifest_individual_lines():
    expected_lines = [
        "/home/user/build_env/java/java-home -> jdk-17.0.9 [OK]",
        "/home/user/build_env/ndk/ndk-current -> ndk-r26b [OK]",
        "/home/user/build_env/sdks/current-sdk -> android-34 [OK]",
        "/home/user/build_env/tools/build-tools-active -> build-tools-34.0.0 [OK]",
        "/home/user/build_env/tools/ndk-active -> /home/user/build_env/ndk/ndk-r26b [OK]",
    ]
    with open(MANIFEST, "r") as f:
        actual_lines = [line.rstrip("\n") for line in f if line.strip()]
    for expected in expected_lines:
        assert expected in actual_lines, (
            f"Expected line not found in {MANIFEST}:\n"
            f"  Expected: {expected!r}\n"
            f"  Actual lines: {actual_lines}"
        )