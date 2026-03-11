I'm a DevSecOps engineer and I need to enforce a backup policy for our compliance policy files. We have a directory at `/home/user/compliance` that contains various files — some are policy definitions we must archive, and others are temporary or draft files that must be excluded.

**Your task:**

Create a compressed archive of only the files in `/home/user/compliance` that match the pattern `*_policy.yml` (files ending in `_policy.yml`). Then generate a SHA-256 checksum file for the archive.

**Specifics:**

1. Create a gzip-compressed tar archive at `/home/user/backups/policies.tar.gz` containing only the `*_policy.yml` files from `/home/user/compliance`. The files should be archived **without any leading path components** — meaning when extracted, they appear directly as bare filenames (e.g., `access_policy.yml`, not `home/user/compliance/access_policy.yml` or `./compliance/access_policy.yml`). Do not recurse into subdirectories.

2. Generate a SHA-256 checksum of `/home/user/backups/policies.tar.gz` and write it to `/home/user/backups/policies.tar.gz.sha256`. The file must contain exactly one line in this format:
   ```
   <sha256hex>  policies.tar.gz
   ```
   That is: the 64-character hex digest, followed by **two spaces**, followed by the bare filename `policies.tar.gz` (not the full path), and a trailing newline. This is the standard `sha256sum` output format.

The `/home/user/backups/` directory needs to be created if it doesn't already exist.
