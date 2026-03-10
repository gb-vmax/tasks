I'm a backup administrator and I need your help archiving some project data. Here's the situation:

There's a directory at `/home/user/projects/client_alpha` that contains several files I need to back up. I need you to create a compressed tar archive of that entire directory and then record some metadata about the backup.

Please do the following:

1. Create a gzip-compressed tar archive of `/home/user/projects/client_alpha` and save it to `/home/user/backups/client_alpha.tar.gz`. The archive should preserve the directory structure (i.e., extracting it should recreate a `client_alpha` directory containing all the files).

2. After creating the archive, write a backup manifest file at `/home/user/backups/manifest.txt` with exactly the following format:

```
archive: client_alpha.tar.gz
size_bytes: <size>
files: <count>
```

Where:
- `<size>` is the size of the archive file `client_alpha.tar.gz` in bytes (as reported by `ls -l` or `stat` — the exact byte count of the `.tar.gz` file itself, not the uncompressed content)
- `<count>` is the total number of files inside the archive (not counting directories, only regular files)

The manifest must have exactly three lines in that order, with no extra whitespace, trailing spaces, or blank lines.
