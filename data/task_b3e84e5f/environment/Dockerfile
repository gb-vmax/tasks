FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the appdata directory structure
mkdir -p /home/user/appdata/{logs,cache,db,uploads,config,tmp}

# logs: ~300KB
dd if=/dev/urandom of=/home/user/appdata/logs/app.log bs=1024 count=300 2>/dev/null

# uploads: ~200KB
dd if=/dev/urandom of=/home/user/appdata/uploads/data.bin bs=1024 count=200 2>/dev/null

# db: ~150KB
dd if=/dev/urandom of=/home/user/appdata/db/records.db bs=1024 count=150 2>/dev/null

# cache: ~100KB
dd if=/dev/urandom of=/home/user/appdata/cache/objects.bin bs=1024 count=100 2>/dev/null

# tmp: ~50KB
dd if=/dev/urandom of=/home/user/appdata/tmp/scratch.bin bs=1024 count=50 2>/dev/null

# config: ~4KB (just a small file)
echo "key=value" > /home/user/appdata/config/settings.conf

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
