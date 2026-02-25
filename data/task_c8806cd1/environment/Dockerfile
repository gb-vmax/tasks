FROM ubuntu:22.04

RUN <<'ENDPOST'
set -eux

# Create user and home directory
useradd -m -s /bin/bash user

# Install required packages
apt-get update
apt-get install -y --no-install-recommends \
    git \
    python3 \
    python3-pip

# Install pytest for testing
pip3 install --no-cache-dir pytest

# Ensure user owns their home directory
chown -R user:user /home/user
ENDPOST

WORKDIR /home/user
