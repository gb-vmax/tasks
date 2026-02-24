FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin:$PATH

RUN <<'ENDPOST'
apt-get update
apt-get install -y python3-pip
pip3 install pytest
# Add user for /home/user (if needed)
if ! id user >/dev/null 2>&1; then
    useradd -m -s /bin/bash user
fi
chown -R user:user /home/user
ENDPOST

WORKDIR /home/user
