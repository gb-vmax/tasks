FROM ubuntu:22.04

RUN <<'ENDPOST'
set -eux

    # Create user 'user' with home directory
    useradd -m -s /bin/bash user

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest

    # Create source configs directory and nginx.conf as user
    su - user -c 'mkdir -p /home/user/source_configs'
    su - user -c 'cat > /home/user/source_configs/nginx.conf <<EOF
user www-data;
worker_processes auto;
pid /run/nginx.pid;
EOF
'

    # Create remote_server/configs directory as user
    su - user -c 'mkdir -p /home/user/remote_server/configs'

    # Simulate rsync: copy file, preserve ownership
    su - user -c 'cp /home/user/source_configs/nginx.conf /home/user/remote_server/configs/nginx.conf'

    # Create sync.log with the correct line
    su - user -c "echo 'COPIED: /home/user/remote_server/configs/nginx.conf' > /home/user/sync.log"

    # Set permissions (755 for directories is default, but ensure it)
    chmod 755 /home/user/source_configs
    chmod 755 /home/user/remote_server
    chmod 755 /home/user/remote_server/configs

    # Informative message
    echo "Synchronization finished and log generated."
ENDPOST

WORKDIR /home/user
