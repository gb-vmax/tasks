FROM ubuntu:22.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN <<'ENDPOST'
apt-get update
    apt-get install -y python3-pip
    pip3 install pytest

    # Create the required directory
    mkdir -p /home/user/storage

    # Create the config.ini file with exact required contents and permissions
    cat > /home/user/storage/config.ini <<EOF
[disk_thresholds]
/data1 = 80G
/backup = 120G
/var/log = 50G
EOF
    chmod 644 /home/user/storage/config.ini
    chown root:root /home/user/storage/config.ini

    # Ensure the storage directory permissions are correct for user
    chmod 755 /home/user/storage
    chown root:root /home/user/storage
ENDPOST

WORKDIR /home/user
