FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e
apt-get update
apt-get install -y python3-pip python3-setuptools python3-wheel
pip3 install --no-cache-dir pytest

# Create the user "user" with home directory /home/user if not exists
if ! id "user" >/dev/null 2>&1; then
    useradd -m -s /bin/bash user
fi

# Ensure /home/user exists and is owned by user
mkdir -p /home/user
chown user:user /home/user

# Create the deployments and analytics-app parent directories (agent will handle analytics-app itself)
mkdir -p /home/user/deployments
chown user:user /home/user/deployments
ENDPOST

WORKDIR /home/user
