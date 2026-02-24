FROM ubuntu:22.04

ENV PATH=/home/user/.local/bin:$PATH

RUN <<'ENDPOST'
set -e

# Create user and home directory
useradd -m -d /home/user user

# Ensure home directory exists and is writable
chmod 755 /home/user
chown user:user /home/user

# Install Python 3, venv, pip, and other tools
apt-get update
apt-get install -y python3 python3-venv python3-pip python3-setuptools python3-wheel

# Install pytest for testing
pip3 install pytest
ENDPOST

WORKDIR /home/user
