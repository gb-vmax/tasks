I'm a mobile build engineer and I need your help maintaining our CI/CD build pipeline on our Linux build server. The pipeline relies heavily on symbolic links to switch between Android SDK versions and build tools without modifying every Makefile and CI script. Our setup has gotten messy — some symlinks are broken, some point to outdated targets, and we need to add new ones for a new NDK version we just installed.

The build environment lives at `/home/user/build_env`. Here's what I need you to do:

---

### 1. Fix the broken `current-sdk` symlink

There is a symlink at `/home/user/build_env/sdks/current-sdk` that is broken (its target no longer exists). It should instead point to `/home/user/build_env/sdks/android-34`. Update it to point to the correct target. The symlink itself must stay at the same path — do not delete it and re-create it somewhere else. It must be a relative symlink pointing to `android-34` (not an absolute path).

### 2. Repoint the `build-tools-active` symlink

There is a symlink at `/home/user/build_env/tools/build-tools-active` that currently points to `build-tools-33.0.1`. Repoint it to `build-tools-34.0.0` instead. This must also be a relative symlink (just `build-tools-34.0.0`, not a full absolute path).

### 3. Create NDK symlinks

A new NDK has been installed at `/home/user/build_env/ndk/ndk-r26b`. Create the following two symlinks:

- `/home/user/build_env/ndk/ndk-current` → relative target `ndk-r26b`
- `/home/user/build_env/tools/ndk-active` → this one must be an **absolute** symlink pointing to `/home/user/build_env/ndk/ndk-r26b`

### 4. Create a `java-home` convenience symlink

Our build scripts reference `/home/user/build_env/java/java-home`. Create this as a relative symlink pointing to `jdk-17.0.9` (which exists at `/home/user/build_env/java/jdk-17.0.9`).

### 5. Generate a symlink manifest report

After all changes are in place, generate a report file at `/home/user/build_env/symlink_manifest.txt`. The report must list every symbolic link under `/home/user/build_env` (search recursively), sorted alphabetically by the symlink's full path. 

Each line must follow this exact format:
```
<full_path_to_symlink> -> <link_target> [<status>]
```

Where:
- `<full_path_to_symlink>` is the absolute path to the symlink
- `<link_target>` is exactly what the symlink stores as its target (i.e., what `readlink` returns — relative if it was created relative, absolute if absolute)
- `<status>` is either `OK` if the symlink resolves to an existing file/directory, or `BROKEN` if it does not

The symlink_manifest.txt file itself should NOT appear in the manifest (since it's not a symlink). 

Example lines (not real values):
```
/home/user/build_env/foo/bar-link -> ../baz [OK]
/home/user/build_env/foo/missing-link -> ../gone [BROKEN]
```

There must be no trailing spaces on any line. The file must end with a newline.

---

**Summary of what I need verified:**
- `current-sdk` symlink is fixed and relative
- `build-tools-active` symlink is repointed and relative
- Two new NDK symlinks exist (one relative, one absolute)
- `java-home` symlink exists and is relative
- `symlink_manifest.txt` is generated with correct format, correct status flags, alphabetically sorted
