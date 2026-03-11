#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/artifact-repo/{releases,snapshots,cache}
chmod 755 /home/user/artifact-repo/releases && chmod 750 /home/user/artifact-repo/snapshots && chmod 700 /home/user/artifact-repo/cache
cat > /home/user/artifact-repo/repo.conf << 'EOF'
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
EOF
ls -ld /home/user/artifact-repo/releases /home/user/artifact-repo/snapshots /home/user/artifact-repo/cache && echo "---" && cat /home/user/artifact-repo/repo.conf
