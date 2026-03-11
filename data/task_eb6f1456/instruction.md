I'm a compliance analyst and I need to create an audit archive for our quarterly review. I have a directory of application logs at `/home/user/audit_logs/` that contains several `.log` files. I need to package the logs into a compressed archive and then generate a SHA256 checksum file so that we can verify the archive hasn't been tampered with later.

Here's exactly what I need you to do:

1. Create a gzip-compressed tar archive of **all `.log` files** in `/home/user/audit_logs/` (do not include subdirectories, just the files directly in that directory). The archive should be saved to `/home/user/archive/Q3_audit.tar.gz`. The `audit_logs` directory itself should be included as the path prefix inside the archive (i.e., files inside the archive should appear as `audit_logs/access.log`, `audit_logs/error.log`, etc., not as bare filenames).

2. Generate a SHA256 checksum of the archive file and write it to `/home/user/archive/Q3_audit.tar.gz.sha256`. The file must contain exactly one line in the standard `sha256sum` output format:

```
<64-char hex digest>  Q3_audit.tar.gz
```

That is: the hash, two spaces, then just the **filename** (not the full path), followed by a newline. This format must be exactly reproducible so that running `sha256sum -c Q3_audit.tar.gz.sha256` from inside `/home/user/archive/` would pass verification.

Please make sure the `/home/user/archive/` directory exists before writing to it. The final state should be two files in `/home/user/archive/`: `Q3_audit.tar.gz` and `Q3_audit.tar.gz.sha256`.
