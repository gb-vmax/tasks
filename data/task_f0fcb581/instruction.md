I'm a build engineer managing a release artifact directory for a multi-component software project. I need your help setting up a proper versioned artifact tree with symbolic links so our deployment tooling can always find the "current" and "latest-stable" builds without hardcoding paths. I also need a manifest file generated from the final state of the symlinks.

Here's the situation: we have a directory at `/home/user/artifacts` that already has some versioned build outputs in it. I need you to do the following end-to-end:

---

**1. Inspect what's already there**

The `/home/user/artifacts/builds/` directory contains versioned subdirectories. Each subdirectory is named after a build version like `2.1.0`, `2.2.0`, `2.3.0-beta`, `2.3.1`, etc. Inside each version directory, there is a file called `app.tar.gz` and a file called `build.meta` (which contains a single line like `status=stable` or `status=beta`).

---

**2. Create a `releases/` directory structure with versioned symlinks**

Under `/home/user/artifacts/releases/`, create symbolic links for each version found in `/home/user/artifacts/builds/`. Each symlink should:
- Be named after the version (e.g., `2.1.0`)
- Point to the corresponding absolute path in `builds/` (e.g., `/home/user/artifacts/builds/2.1.0`)

So after this step, `/home/user/artifacts/releases/2.1.0` is a symlink to `/home/user/artifacts/builds/2.1.0`, and so on for all versions.

---

**3. Create a `current` symlink**

In `/home/user/artifacts/releases/`, create a symlink named `current` that points to the **highest stable version** directory (i.e., the version whose `build.meta` contains `status=stable` with the greatest version number using standard semantic versioning sort order — beta builds must be excluded). The symlink should point to the absolute path of that version's directory inside `builds/`.

---

**4. Create a `latest-stable` symlink in `/home/user/artifacts/`**

Create a symlink at `/home/user/artifacts/latest-stable` that points to `/home/user/artifacts/releases/current` (i.e., it chains through the `releases/current` symlink — it does NOT directly point to the build directory).

---

**5. Create a `latest-beta` symlink in `/home/user/artifacts/`**

Create a symlink at `/home/user/artifacts/latest-beta` that points to the absolute path of the **highest beta version** directory inside `builds/` (the one whose `build.meta` contains `status=beta` with the greatest version number). If there are no beta builds, skip this step.

---

**6. Reassign the `current` symlink to the correct target if needed**

After double-checking, verify that `/home/user/artifacts/releases/current` is a symlink and that it resolves (via `readlink`) to the correct absolute path. If it was created incorrectly, fix it. This is a verification/correction step.

---

**7. Generate a manifest file**

Write a manifest file to `/home/user/artifacts/manifest.txt`. The manifest must contain exactly the following sections and format — automated tooling will parse it line by line:

```
=== ARTIFACT MANIFEST ===
generated: <date in YYYY-MM-DD format using current system date>

[releases]
<version>: <absolute symlink target>
<version>: <absolute symlink target>
...

[special]
current -> <absolute path that releases/current points to>
latest-stable -> <absolute path that /home/user/artifacts/latest-stable points to>
latest-beta -> <absolute path that /home/user/artifacts/latest-beta points to>

[resolution]
latest-stable resolves to: <the fully resolved real path that latest-stable ultimately points to>
latest-beta resolves to: <the fully resolved real path that latest-beta ultimately points to>
```

Specific formatting rules:
- The `[releases]` section must list all version symlinks (excluding `current`) in **ascending semantic version order** (stable and beta alike, betas sorted before the same-number stable, i.e., `2.3.0-beta` before `2.3.1`). Use a plain alphanumeric sort is NOT acceptable — use semantic version ordering.
- Each release line format is exactly: `<version>: <target>` where target is the absolute path the symlink points to (from `readlink`, not `realpath`).
- In the `[special]` section, each line format is exactly: `<name> -> <target>` where target is the direct symlink target (from `readlink`).
- In the `[resolution]` section, use `realpath` or equivalent to show the fully resolved final path (no symlinks remaining in the path).
- There must be a blank line between the header block (`generated:` line) and `[releases]`, between `[releases]` block and `[special]`, and between `[special]` block and `[resolution]`.
- The `latest-beta` line in `[special]` and `[resolution]` must still appear even if the path points to a beta build.

---

**Summary of files and symlinks expected to exist when done:**
- `/home/user/artifacts/releases/2.1.0` → symlink to `/home/user/artifacts/builds/2.1.0`
- `/home/user/artifacts/releases/2.2.0` → symlink to `/home/user/artifacts/builds/2.2.0`
- `/home/user/artifacts/releases/2.3.0-beta` → symlink to `/home/user/artifacts/builds/2.3.0-beta`
- `/home/user/artifacts/releases/2.3.1` → symlink to `/home/user/artifacts/builds/2.3.1`
- `/home/user/artifacts/releases/current` → symlink to `/home/user/artifacts/builds/2.3.1` (highest stable)
- `/home/user/artifacts/latest-stable` → symlink to `/home/user/artifacts/releases/current`
- `/home/user/artifacts/latest-beta` → symlink to `/home/user/artifacts/builds/2.3.0-beta`
- `/home/user/artifacts/manifest.txt` → regular file with the manifest

Please carry out all of these steps in the terminal.
