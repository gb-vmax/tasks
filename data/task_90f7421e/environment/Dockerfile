FROM ubuntu:22.04

ENV PATH="$PATH:/home/user/.local/bin"

RUN <<'ENDPOST'
set -e

# Install necessary packages
apt-get update
apt-get install -y python3-pip openssh-client

# Create a non-root user 'user' with home directory /home/user
useradd -m -s /bin/bash user

# Create .ssh directory with correct permissions
mkdir -p /home/user/.ssh
chown user:user /home/user/.ssh
chmod 700 /home/user/.ssh

# Install pytest for the user
pip3 install --no-cache-dir pytest
# Also make pytest available for 'user'
pip3 install --no-cache-dir --user pytest
ENDPOST

WORKDIR /home/user
