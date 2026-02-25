FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin:$PATH

RUN <<'ENDPOST'
set -e

# Install ping (iputils-ping), tar, gzip, python3-pip for pytest
apt-get update
apt-get install -y --no-install-recommends \
    iputils-ping \
    tar \
    gzip \
    python3-pip

# Install pytest
pip3 install --no-cache-dir pytest

# Create user and directories
useradd -m user || true

mkdir -p /home/user/network/backup

# Set permissions so user can write
chown -R user:user /home/user
chmod 700 /home/user/network
chmod 700 /home/user/network/backup
ENDPOST

WORKDIR /home/user
