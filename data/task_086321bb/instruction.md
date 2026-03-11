I'm a compliance analyst and I need to archive last month's audit logs for long-term retention. The raw log files are sitting in `/home/user/audit_logs/2024-02/` and I need to package them up properly with a checksum file so we can verify integrity later.

Here's exactly what I need you to do:

**Step 1: Create a compressed tar archive**

Create a gzip-compressed tar archive of the entire `/home/user/audit_logs/2024-02/` directory. The archive should be saved to `/home/user/backups/audit_2024-02.tar.gz`. The archive should contain the files with paths relative to `/home/user/audit_logs/` (i.e., the paths inside the archive should start with `2024-02/`, not with `/home/user/audit_logs/`). The `/home/user/backups/` directory does not exist yet — you'll need to create it first.

**Step 2: Generate a SHA256 checksum file**

After creating the archive, generate a SHA256 checksum of the archive file `audit_2024-02.tar.gz` and write it to `/home/user/backups/audit_2024-02.tar.gz.sha256`.

The checksum file must contain exactly one line in the standard `sha256sum` output format:
```
<64-hex-char-hash>  audit_2024-02.tar.gz
```

Note that there are **two spaces** between the hash and the filename, and the filename is just the bare filename (not a full path). The file should end with a newline.

This checksum file is what our compliance tooling will use to verify the archive hasn't been tampered with, so the format must be exact.
