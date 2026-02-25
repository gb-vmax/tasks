FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

# Install python3 and pip for pytest
apt-get update
apt-get install -y python3 python3-pip

# Install pytest
pip3 install pytest

# Create user 'user' with home directory /home/user and group 'user'
groupadd -g 1000 user
useradd -m -u 1000 -g user user

# Create scripts directory and deploy.sh file as user:user
mkdir -p /home/user/scripts
touch /home/user/scripts/deploy.sh
chown user:user /home/user/scripts/deploy.sh
chown user:user /home/user/scripts
chmod 755 /home/user/scripts
chmod 644 /home/user/scripts/deploy.sh

# Ensure /home/user exists and is owned by user:user
chown user:user /home/user
ENDPOST

WORKDIR /home/user
