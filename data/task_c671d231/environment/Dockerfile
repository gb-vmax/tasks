FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin

RUN <<'ENDPOST'
apt-get update
apt-get install -y python3-pip
pip3 install --no-cache-dir pytest

# Create /home/user directory with correct permissions if it doesn't exist
mkdir -p /home/user
chown -R 1000:1000 /home/user
chmod 755 /home/user
ENDPOST

WORKDIR /home/user
