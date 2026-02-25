FROM ubuntu:22.04

ENV PATH=/home/user/.local/bin:$PATH

RUN <<'ENDPOST'
set -eux
# Create user with home directory
useradd -m user

# Update package lists
apt-get update

# Install python3-pip and pytest
apt-get install -y python3-pip
pip3 install pytest

# Clean up apt cache to reduce image size
apt-get clean
rm -rf /var/lib/apt/lists/*

# Ensure /home/user has correct permissions
chown -R user:user /home/user
ENDPOST

WORKDIR /home/user
