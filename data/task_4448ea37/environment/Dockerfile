FROM endless-base:latest

ENV PATH=/usr/local/bin:/usr/bin:/bin

RUN <<'ENDPOST'
set -e
apt-get update
apt-get install -y python3-pip
pip3 install pytest

# Ensure /home/user exists and is owned by a non-root user
if ! id user >/dev/null 2>&1; then
    useradd -m -s /bin/bash user
fi
chown -R user:user /home/user
ENDPOST

WORKDIR /home/user
