FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install python3-pip and pytest
    apt-get update
    apt-get install -y python3 python3-pip
    pip3 install pytest

    # Create user and home directory if not present
    useradd -m user || true
    mkdir -p /home/user/alert_scripts

    # Create check_disk.sh with the correct initial contents
    cat > /home/user/alert_scripts/check_disk.sh <<'EOF'
# Version: 1.2.3
#!/bin/bash
# Script to check disk space and trigger alerts
EOF

    # Ensure user read/write permissions for check_disk.sh
    chown user:user /home/user/alert_scripts/check_disk.sh
    chmod 600 /home/user/alert_scripts/check_disk.sh

    # Ensure directory is owned by user and is accessible
    chown -R user:user /home/user/alert_scripts
    chmod 700 /home/user/alert_scripts
ENDPOST

WORKDIR /home/user
