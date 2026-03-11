I'm a backup operator and I need to verify that a system restore went correctly. I have a backup archive and a manifest file from before the "disaster", and I need to compare what Python packages are currently installed against what was recorded in the manifest, then produce a formal restore verification report.

Here's the scenario: a Python environment was backed up, a "disaster" happened, and a restore was attempted. I need to audit whether the restore was complete and accurate.

**Pre-existing files you'll find:**

- `/home/user/backup/packages_manifest.txt` — the original manifest recorded before the disaster, listing packages and versions that should be present after a successful restore
- `/home/user/backup/restore_archive.tar.gz` — the backup archive containing a `site-packages/` directory tree that was supposed to be extracted into the restore target
- `/home/user/restore_target/` — a directory representing the restored environment (already partially populated)

**Your tasks:**

**Step 1: Extract the backup archive**

Extract `/home/user/backup/restore_archive.tar.gz` into `/home/user/restore_work/`. The archive contains a `site-packages/` directory with subdirectories named after packages (e.g., `requests-2.28.1.dist-info/`, `flask-2.2.0.dist-info/`). Each `.dist-info` directory contains a `METADATA` file with at least a `Name:` line and a `Version:` line.

**Step 2: Parse the backup archive's package list**

From the extracted `.dist-info` directories under `/home/user/restore_work/site-packages/`, build a list of packages and their versions. The package name comes from the `Name:` field in `METADATA`, and the version comes from the `Version:` field. These represent what SHOULD have been restored.

**Step 3: Parse the restore target's package list**

The restore target is at `/home/user/restore_target/site-packages/`. It also contains `.dist-info` directories with `METADATA` files. Parse these the same way to find what IS currently installed.

**Step 4: Compare and classify**

Compare the two lists (archive vs restore target). Classify each package from the manifest (archive) into one of these categories:

- `OK` — package is present in restore target with the correct version
- `WRONG_VERSION` — package is present in restore target but with a different version
- `MISSING` — package is not present in the restore target at all

Also note any packages present in the restore target that are NOT in the archive manifest as `EXTRA`.

**Step 5: Write the restore verification report**

Write the report to `/home/user/restore_report.txt` with this EXACT format:

```
=== RESTORE VERIFICATION REPORT ===
Archive: /home/user/backup/restore_archive.tar.gz
Target: /home/user/restore_target/site-packages

--- PACKAGE STATUS ---
<package_name>==<archive_version> [OK]
<package_name>==<archive_version> -> <target_version> [WRONG_VERSION]
<package_name>==<archive_version> [MISSING]

--- EXTRA PACKAGES IN TARGET ---
<package_name>==<target_version> [EXTRA]

--- SUMMARY ---
Total packages in archive: <N>
OK: <N>
WRONG_VERSION: <N>
MISSING: <N>
EXTRA: <N>
Restore status: <STATUS>
```

Formatting rules:
- In the `PACKAGE STATUS` section, list all packages from the archive sorted **alphabetically by lowercase package name**.
- For `OK` entries: `<name>==<version> [OK]`
- For `WRONG_VERSION` entries: `<name>==<archive_version> -> <target_version> [WRONG_VERSION]`
- For `MISSING` entries: `<name>==<version> [MISSING]`
- In the `EXTRA PACKAGES IN TARGET` section, list extra packages sorted alphabetically. If there are no extra packages, write `None`.
- `Restore status` must be `SUCCESS` if there are zero MISSING and zero WRONG_VERSION packages (EXTRA packages are acceptable); otherwise it must be `INCOMPLETE`.
- Package names should be used exactly as they appear in the `Name:` field of the METADATA files (preserve original casing for display).
