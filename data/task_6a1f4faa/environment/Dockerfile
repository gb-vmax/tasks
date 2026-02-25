FROM ubuntu:22.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN <<'ENDPOST'
set -e

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest

    # Create user and home directory if not present
    useradd -m -d /home/user user || true

    # Create /home/user/targets.txt with the required content
    mkdir -p /home/user
    cat > /home/user/targets.txt <<EOF
web1.corp.local
192.168.10.5
dbserver.corp.local
router01
EOF

    # Set permissions so non-root users can read/write as needed
    chown -R user:user /home/user
    chmod 755 /home/user
    chmod 644 /home/user/targets.txt
ENDPOST

WORKDIR /home/user
