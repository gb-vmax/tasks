FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the archive directory structure
mkdir -p /home/user/archive/videos
mkdir -p /home/user/archive/docs
mkdir -p /home/user/archive/logs
mkdir -p /home/user/archive/configs

# Create binary files with exact sizes
dd if=/dev/zero of=/home/user/archive/videos/clip.bin bs=1024 count=40
dd if=/dev/zero of=/home/user/archive/docs/manual.bin bs=1024 count=20
dd if=/dev/zero of=/home/user/archive/logs/app.bin bs=1024 count=8
dd if=/dev/zero of=/home/user/archive/configs/settings.bin bs=1024 count=4

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
