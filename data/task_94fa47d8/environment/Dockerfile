FROM ubuntu:22.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV PATH=/home/user/.local/bin:$PATH

RUN <<'ENDPOST'
set -eux

# Install Python3, pip, and curl
apt-get update
apt-get install -y python3 python3-pip curl

# Install pytest for testing
pip3 install pytest

# Create the user with home directory if not already present
if ! id user >/dev/null 2>&1; then
    useradd -m -d /home/user user
fi

# Give user ownership of home directory
chown -R user:user /home/user
ENDPOST

WORKDIR /home/user
