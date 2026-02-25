FROM ubuntu:22.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN <<'ENDPOST'
set -e

    # Ensure user and home directory exist
    groupadd -g 1000 user || true
    useradd -m -u 1000 -g 1000 user || true

    # Install Python3, pip, and pytest
    apt-get update
    apt-get install -y python3 python3-pip
    pip3 install --no-cache-dir pytest

    # Create the initial server_inventory.csv file in /home/user with correct permissions
    mkdir -p /home/user
    cat > /home/user/server_inventory.csv <<EOF
hostname,ip_address,os_type,provisioned
srv1,10.0.0.1,ubuntu,no
srv2,10.0.0.2,centos,yes
srv3,10.0.0.3,debian,no
EOF
    chown user:user /home/user/server_inventory.csv
    chmod 644 /home/user/server_inventory.csv

    # Set ownership of /home/user
    chown -R user:user /home/user
ENDPOST

WORKDIR /home/user
