I'm a backup administrator and I need to archive some important project data before decommissioning a server. I have a directory at `/home/user/projects/website` that contains source files and configuration files across two subdirectories. I need you to create a compressed tar archive of this directory and then verify it was created correctly.

Here's exactly what I need:

1. Create a gzip-compressed tar archive of the entire `/home/user/projects/website` directory. The archive should be saved to `/home/user/backups/website_backup.tar.gz`. The archive must preserve the directory structure (i.e., paths inside the archive should be relative, starting with `website/`, not absolute paths like `/home/user/projects/website/...`).

2. After creating the archive, write a verification file at `/home/user/backups/website_backup.manifest` that lists every file contained inside the archive, one file per line, exactly as reported by `tar -tzf`. The manifest file must contain only the file/directory listing with no extra headers, footers, or commentary — just the raw output of listing the archive contents.

The directory `/home/user/backups/` may not exist yet, so you'll need to create it if necessary.

Please make sure the archive is actually valid and readable — the automated check will decompress it and compare its contents against the manifest file.
