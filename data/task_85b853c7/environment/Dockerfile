FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the base directory structure
mkdir -p /home/user/server_data/logs
mkdir -p /home/user/server_data/backups
mkdir -p /home/user/server_data/cache
mkdir -p /home/user/server_data/tmp
mkdir -p /home/user/server_data/sessions

# Create files with exact sizes
# logs/app.log: 102400 bytes (100 KB)
dd if=/dev/zero of=/home/user/server_data/logs/app.log bs=1024 count=100

# backups/backup.tar: 204800 bytes (200 KB)
dd if=/dev/zero of=/home/user/server_data/backups/backup.tar bs=1024 count=200

# cache/cache.db: 65536 bytes (64 KB)
dd if=/dev/zero of=/home/user/server_data/cache/cache.db bs=1024 count=64

# tmp/scratch.txt: 8192 bytes (8 KB)
dd if=/dev/zero of=/home/user/server_data/tmp/scratch.txt bs=1024 count=8

# sessions/sess.dat: 32768 bytes (32 KB)
dd if=/dev/zero of=/home/user/server_data/sessions/sess.dat bs=1024 count=32

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
