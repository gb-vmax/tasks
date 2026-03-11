Hey, I need your help archiving some old release binaries that we're moving to cold storage. I manage a binary artifact repository and I need to create a proper compressed archive of the `v2.4.0` release artifacts, then generate a SHA-256 checksum file so we can verify integrity later.

The release artifacts are located in `/home/user/artifacts/v2.4.0/`. This directory contains several binary files that need to be archived together.

Here's exactly what I need you to do:

**Step 1: Create the archive**

Create a gzip-compressed tar archive of the entire `/home/user/artifacts/v2.4.0/` directory. The archive file should be written to `/home/user/backups/v2.4.0-release.tar.gz`. The archive should preserve the directory structure (i.e., when extracted, it should recreate a `v2.4.0/` directory containing all the files). Make sure the `/home/user/backups/` directory exists before writing to it.

**Step 2: Generate the checksum file**

After creating the archive, generate a SHA-256 checksum of `/home/user/backups/v2.4.0-release.tar.gz` and write it to `/home/user/backups/v2.4.0-release.tar.gz.sha256`.

The checksum file must contain exactly one line in this format:
```
<sha256hash>  v2.4.0-release.tar.gz
```
That is: the 64-character hex digest, followed by **two spaces**, followed by just the filename `v2.4.0-release.tar.gz` (no directory path). This is the standard format produced by `sha256sum`.

The file must end with a newline. No extra lines, no extra spaces.

After you're done, both files should exist in `/home/user/backups/`:
- `v2.4.0-release.tar.gz`
- `v2.4.0-release.tar.gz.sha256`

And running `sha256sum --check /home/user/backups/v2.4.0-release.tar.gz.sha256` from the `/home/user/backups/` directory should exit with status 0 and print `v2.4.0-release.tar.gz: OK`.
