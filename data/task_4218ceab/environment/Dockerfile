FROM ubuntu:22.04

ENV PATH="/home/user/.local/bin:$PATH"

RUN <<'ENDPOST'
set -eux

# Create the user and home directory with proper permissions
useradd -m -d /home/user user
chown user:user /home/user
chmod 755 /home/user

# Install pip and pytest (python3-pip is in Ubuntu 22.04)
apt-get update
apt-get install -y python3-pip
pip3 install --no-cache-dir pytest

# Clean up apt cache to keep image small
apt-get clean
rm -rf /var/lib/apt/lists/*
ENDPOST

WORKDIR /home/user
