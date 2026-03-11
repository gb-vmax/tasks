I'm a backup administrator and I need to securely archive a set of configuration files before a system migration. The files are stored in `/home/user/configs/` directory. I need to create a compressed tarball of the entire directory, verify the archive is intact, and then generate a SHA-256 checksum file so our security team can validate the archive's authenticity later.

Here's exactly what I need you to do:

**Step 1: Create the archive**

Create a gzip-compressed tar archive of `/home/user/configs/` and save it to `/home/user/backups/configs_backup.tar.gz`. The archive should include all files inside the `configs` directory.

**Step 2: Verify the archive**

Test the integrity of `/home/user/backups/configs_backup.tar.gz` to confirm it is a valid, non-corrupt gzip tar archive. If the test fails for any reason, do not proceed further.

**Step 3: Generate the checksum file**

Compute the SHA-256 checksum of `/home/user/backups/configs_backup.tar.gz` and write it to `/home/user/backups/configs_backup.tar.gz.sha256`.

The checksum file must contain exactly one line in the following format (this is the standard output format of `sha256sum`):

```
<64-character-hex-hash>  /home/user/backups/configs_backup.tar.gz
```

Note the **two spaces** between the hash and the filename. The filename in the checksum file must be the full absolute path `/home/user/backups/configs_backup.tar.gz`, not a relative path or just the filename. The file must end with a newline character.

**Step 4: Verify the checksum**

Run `sha256sum --check` against `/home/user/backups/configs_backup.tar.gz.sha256` from the `/home/user/backups/` directory to confirm the checksum verifies successfully. The output should confirm the archive passes: you should see output containing `configs_backup.tar.gz: OK`.

The `/home/user/backups/` directory already exists. When I inspect `/home/user/backups/configs_backup.tar.gz.sha256` afterwards, it should have exactly one line matching the format above, and running `sha256sum --check /home/user/backups/configs_backup.tar.gz.sha256` from any directory should succeed (exit code 0) because the file path inside is absolute.
