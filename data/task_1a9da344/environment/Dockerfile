FROM ubuntu:22.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN <<'ENDPOST'
set -eux

# Install Python3, pip, and pytest
apt-get update
apt-get install -y python3 python3-pip

pip3 install --no-cache-dir pytest

# Install sqlite3 CLI tool
apt-get install -y sqlite3

# Create the user home directory with correct permissions
useradd -m user || true
mkdir -p /home/user
chown -R 1000:1000 /home/user
ENDPOST

WORKDIR /home/user
