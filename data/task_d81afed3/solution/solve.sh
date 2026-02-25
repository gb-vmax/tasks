#!/bin/bash
set -euo pipefail

# The Dockerfile environment already sets up the correct final state.
# This solve.sh ensures the state is correct by (re)creating files if needed.

# Create source_configs directory and nginx.conf
mkdir -p /home/user/source_configs
cat > /home/user/source_configs/nginx.conf << 'EOF'
user www-data;
worker_processes auto;
pid /run/nginx.pid;
EOF

# Create remote_server/configs directory
mkdir -p /home/user/remote_server/configs

# Copy nginx.conf to remote location
cp /home/user/source_configs/nginx.conf /home/user/remote_server/configs/nginx.conf

# Create sync log
printf 'COPIED: /home/user/remote_server/configs/nginx.conf\n' > /home/user/sync.log

# Fix ownership if running as root
if [ "$(id -u)" = "0" ] && id user >/dev/null 2>&1; then
    chown user:user /home/user/source_configs /home/user/source_configs/nginx.conf
    chown user:user /home/user/remote_server /home/user/remote_server/configs /home/user/remote_server/configs/nginx.conf
    chown user:user /home/user/sync.log
fi
