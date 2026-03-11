I'm an artifact manager and I need to archive a specific set of release binaries from our build repository for long-term storage. The binaries are stored under `/home/user/artifacts/` in versioned subdirectories.

Here's what I need you to do:

**Step 1: Create a compressed archive**

Archive only the files whose names end in `.bin` or `.so` found anywhere under `/home/user/artifacts/`. The archive should be named `release_bundle.tar.gz` and placed at `/home/user/backup/release_bundle.tar.gz`. The archive should preserve the directory structure relative to `/home/user/artifacts/` (i.e., paths inside the archive should look like `v1.0/app.bin`, not `/home/user/artifacts/v1.0/app.bin` or `home/user/artifacts/v1.0/app.bin`).

**Step 2: Generate a SHA256 checksum file**

Compute the SHA256 checksum of `release_bundle.tar.gz` and write it to `/home/user/backup/release_bundle.tar.gz.sha256`. The file must contain exactly one line in the standard `sha256sum` output format:

```
<hash>  release_bundle.tar.gz
```

That is: the 64-character hex digest, two spaces, then the bare filename (not a path), followed by a newline. The file must be suitable for verification with `sha256sum -c` when run from `/home/user/backup/`.

**Step 3: Write a manifest**

Produce a plain-text manifest at `/home/user/backup/MANIFEST.txt` listing every `.bin` and `.so` file that was included in the archive. Each line should contain the file's path as it appears inside the archive (e.g., `v1.0/app.bin`), followed by a single space, followed by its size in bytes. Lines must be sorted alphabetically. The file should end with a newline. No blank lines, no headers, no trailing spaces.

Example of valid manifest lines:
```
v1.0/app.bin 204800
v1.2/librender.so 81920
```

Please make sure `/home/user/backup/` exists before writing any files there.
