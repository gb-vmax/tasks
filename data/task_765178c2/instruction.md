I'm about to roll out a new version of our application and I need to back up the current deployment before making any changes. Can you help me archive the existing deployment directory and create a checksum file so we can verify the backup later?

Here's what I need you to do:

1. Create a gzip-compressed tar archive of the directory `/home/user/deployments/app-v2.3.1` and save it to `/home/user/backups/app-v2.3.1.tar.gz`. The archive should preserve the directory structure (i.e., extracting it should recreate the `app-v2.3.1` directory with all its contents).

2. Generate an SHA-256 checksum of the archive file and write it to `/home/user/backups/app-v2.3.1.tar.gz.sha256`. The file must contain exactly one line in the standard `sha256sum` output format, which looks like:

```
<64-char hex digest>  app-v2.3.1.tar.gz
```

Note: that is two spaces between the hash and the filename — just the filename, not the full path. The file should end with a newline.

The `/home/user/backups/` directory already exists. Do not modify the original `/home/user/deployments/app-v2.3.1` directory in any way.
