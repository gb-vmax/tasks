FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin:$PATH

RUN <<'ENDPOST'
set -eux

# Create the user and home directory
useradd -m -s /bin/bash user

# Install Python 3, venv module, pip, and pytest
apt-get update
apt-get install -y python3 python3-venv python3-pip

# Install pytest system-wide (so user can run pytest without root)
pip3 install pytest

# Ensure /home/user is owned by user
chown -R user:user /home/user
ENDPOST

WORKDIR /home/user
