FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e
apt-get update
apt-get install -y python3-pip
pip3 install pytest

# Create user and home directory if not already present
useradd -m user || true

# Create the config_logs directory with correct permissions
mkdir -p /home/user/config_logs
chown user:user /home/user/config_logs
chmod 755 /home/user/config_logs
ENDPOST

WORKDIR /home/user
