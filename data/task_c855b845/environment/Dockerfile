FROM ubuntu:22.04

RUN <<'ENDPOST'
set -eux

# Install Python3, pip, and pytest
apt-get update
apt-get install -y python3 python3-pip

pip3 install --no-cache-dir pytest

# Create user 'user' with home directory /home/user if not present
if ! id -u user >/dev/null 2>&1; then
    useradd -m -s /bin/bash user
fi

# Create the devops/logs directory with correct ownership and permissions
mkdir -p /home/user/devops/logs
chown -R user:user /home/user/devops
chmod 755 /home/user
chmod 755 /home/user/devops
chmod 755 /home/user/devops/logs
ENDPOST

WORKDIR /home/user
