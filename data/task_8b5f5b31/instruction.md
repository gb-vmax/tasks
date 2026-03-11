Hey, I need help automating a quick backup step in our provisioning pipeline. We have a set of server configuration files that need to be archived before we push any infrastructure changes. This is the "snapshot before deploy" step.

All the configuration files live in `/home/user/infra/configs/`. I need you to do the following:

**Step 1: Create a compressed archive**

Create a gzip-compressed tar archive of the entire `/home/user/infra/configs/` directory. The archive file must be saved to `/home/user/infra/backups/configs_backup.tar.gz`. The archive should preserve the directory structure (i.e., the paths inside the archive should be relative — they should start with `configs/`, not with `/home/user/infra/configs/`). Make sure the `/home/user/infra/backups/` directory exists before creating the archive.

**Step 2: Generate a checksum file**

After the archive is created, generate a SHA-256 checksum of the archive file and write it to `/home/user/infra/backups/configs_backup.tar.gz.sha256`.

The checksum file must contain exactly one line in this format:
```
<sha256hash>  configs_backup.tar.gz
```
That is: the 64-character hex digest, followed by **two spaces**, followed by just the filename (not the full path), followed by a newline. This is the standard `sha256sum` output format — in fact, the file should be produceable by running `sha256sum` on the archive from within the `/home/user/infra/backups/` directory (so the filename portion is just `configs_backup.tar.gz`, not a full path).

**Verification requirement:**

The checksum file must be valid — running `sha256sum --check configs_backup.tar.gz.sha256` from within `/home/user/infra/backups/` must exit with status 0 and print `configs_backup.tar.gz: OK`.

Can you set this up for me?
</think>
