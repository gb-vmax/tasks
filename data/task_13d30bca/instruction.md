I'm setting up a local binary artifact repository manager on my Linux workstation and need help initializing the directory layout and configuration file.

Please do the following:

1. Create the directory structure for the artifact repository under `/home/user/artifact-repo`. It needs these subdirectories:
   - `/home/user/artifact-repo/releases` — for stable release binaries
   - `/home/user/artifact-repo/snapshots` — for development snapshot builds
   - `/home/user/artifact-repo/cache` — for cached upstream artifacts

   The `releases` directory must have permissions `755`.
   The `snapshots` directory must have permissions `750`.
   The `cache` directory must have permissions `700`.

2. Create a configuration file at `/home/user/artifact-repo/repo.conf` with exactly the following content (no extra blank lines, no trailing spaces):

```
[repository]
name=local-artifact-repo
base_path=/home/user/artifact-repo

[storage]
releases_dir=releases
snapshots_dir=snapshots
cache_dir=cache

[policy]
max_cache_size_mb=2048
retain_snapshots=10
retain_releases=all
```

The file must end with a newline after the last line (`retain_releases=all`).
