FROM ubuntu:22.04

ENV LC_ALL=C
ENV PATH=/usr/local/bin:/usr/bin:/bin

RUN <<'ENDPOST'
set -e

# Create the user and home directory
useradd -m -d /home/user user

# Install dependencies: sqlite3, python3-pip (for pytest)
apt-get update
apt-get install -y sqlite3 python3-pip

# Install pytest for the agent's Python environment
pip3 install --no-cache-dir pytest

# Ensure /home/user has the right permissions
chown -R user:user /home/user
ENDPOST

WORKDIR /home/user
