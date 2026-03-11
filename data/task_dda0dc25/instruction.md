I'm a configuration manager and I need your help creating a versioned backup of our application's config directory and recording it in our backup log. Here's what I need done:

We have a configuration directory at `/home/user/configs/` containing several config files. I need you to:

**Step 1: Create a compressed archive**

Create a gzip-compressed tar archive of the entire `/home/user/configs/` directory. Save it to `/home/user/backups/configs_v2.tar.gz`. The archive should store paths relative to `/home/user/` (i.e., entries inside the archive should appear as `configs/app.conf`, not `/home/user/configs/app.conf` or `./configs/app.conf`).

**Step 2: Generate a manifest file**

List the contents of the archive (verbosely) and write the output to `/home/user/backups/configs_v2.manifest`. Use `tar -tzvf` to produce the listing. The manifest should contain exactly what `tar -tzvf /home/user/backups/configs_v2.tar.gz` outputs — do not modify or reformat the lines.

**Step 3: Compute the archive checksum and append to the backup log**

Compute the SHA256 checksum of `/home/user/backups/configs_v2.tar.gz` using `sha256sum`. Then append a single line to `/home/user/backups/backup.log` in this exact format:

```
configs_v2.tar.gz <SHA256_HASH> <SIZE_IN_BYTES>
```

Where:
- `configs_v2.tar.gz` is the literal filename (no path)
- `<SHA256_HASH>` is the 64-character hex digest produced by `sha256sum`
- `<SIZE_IN_BYTES>` is the exact byte size of the archive file as reported by `stat --format="%s"` on the archive

The three fields are separated by single spaces. There should be no trailing spaces or extra characters on the line, and the line must end with a newline.

The file `/home/user/backups/backup.log` already exists with one prior entry — append to it, do not overwrite it.

After you're done, I should be able to:
- Extract `configs_v2.tar.gz` and get back all the config files under a `configs/` directory
- Read `configs_v2.manifest` and see the archive member listing
- Read `backup.log` and see the original entry followed by my new entry on the second line
