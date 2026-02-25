FROM ubuntu:22.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN <<'ENDPOST'
set -e

# Install Python3 and pip
apt-get update
apt-get install -y python3 python3-pip

# Install pytest
pip3 install pytest

# Create the /home/user/workflows directory and set permissions
mkdir -p /home/user/workflows
chown -R 1000:1000 /home/user/workflows
chmod 0775 /home/user/workflows
ENDPOST

WORKDIR /home/user
