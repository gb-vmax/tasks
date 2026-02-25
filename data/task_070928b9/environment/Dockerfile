FROM ubuntu:22.04

RUN <<'ENDPOST'
set -eux

# Install python3-pip and pytest
apt-get update
apt-get install -y python3-pip
pip3 install pytest

# Create user and home directory structure
useradd -m user || true
mkdir -p /home/user/logs/old
mkdir -p /home/user/logs/secure

# Create files with correct permissions
touch /home/user/logs/app.log
chmod 666 /home/user/logs/app.log

touch /home/user/logs/error.log
chmod 640 /home/user/logs/error.log

touch /home/user/logs/old/debug.out
chmod 666 /home/user/logs/old/debug.out

touch /home/user/logs/old/archive.log
chmod 600 /home/user/logs/old/archive.log

touch /home/user/logs/secure/.keep
chmod 644 /home/user/logs/secure/.keep

# Ensure correct ownership for non-root user
chown -R user:user /home/user/logs
ENDPOST

WORKDIR /home/user
