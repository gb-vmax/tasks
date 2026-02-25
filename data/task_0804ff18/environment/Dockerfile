FROM ubuntu:22.04

ENV PATH="/usr/local/bin:$PATH"

RUN <<'ENDPOST'
set -eux

# Create user 'user' with home directory /home/user
useradd -m -s /bin/bash user

apt-get update
apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-setuptools \
    python3-venv

# Make sure pip is up to date
python3 -m pip install --upgrade pip

# Install pytest for testing
python3 -m pip install pytest

# Ensure permissions for /home/user
chown -R user:user /home/user
ENDPOST

WORKDIR /home/user
