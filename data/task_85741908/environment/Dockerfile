FROM ubuntu:22.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN <<'ENDPOST'
set -eux

# Install pip and pytest
apt-get update
apt-get install -y python3-pip
pip3 install --no-cache-dir pytest

# Ensure /home/user exists for the agent's working directory
mkdir -p /home/user
chown 1000:1000 /home/user || true
chmod 755 /home/user
ENDPOST

WORKDIR /home/user
