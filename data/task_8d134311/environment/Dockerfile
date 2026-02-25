FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install Python3, pip, and pytest
    apt-get update
    apt-get install -y python3 python3-pip
    pip3 install --no-cache-dir pytest

    # Create user, project, and bin directories
    mkdir -p /home/user/project/bin

    # Set permissions so non-root can write/read (agent will not have root)
    chown -R 1000:1000 /home/user
    chmod -R 755 /home/user
    chmod 755 /home/user/project
    chmod 755 /home/user/project/bin

    # Create artifacts.ini with the required contents
    cat > /home/user/project/artifacts.ini <<EOF
[artifact1]
version = 1.0.2
path = /home/user/project/bin/artifact1-1.0.2.tar.gz

[artifact2]
version = 2.5.8
path = /home/user/project/bin/artifact2-2.5.8.tar.gz

[artifact3]
version = 0.9.0
path = /home/user/project/bin/artifact3-0.9.0.tar.gz
EOF

    # Create only the artifact1 and artifact3 files, not artifact2
    touch /home/user/project/bin/artifact1-1.0.2.tar.gz
    touch /home/user/project/bin/artifact3-0.9.0.tar.gz

    # Ensure correct permissions for files
    chown 1000:1000 /home/user/project/artifacts.ini
    chown 1000:1000 /home/user/project/bin/artifact1-1.0.2.tar.gz
    chown 1000:1000 /home/user/project/bin/artifact3-0.9.0.tar.gz
    chmod 644 /home/user/project/artifacts.ini
    chmod 644 /home/user/project/bin/artifact1-1.0.2.tar.gz
    chmod 644 /home/user/project/bin/artifact3-0.9.0.tar.gz
ENDPOST

WORKDIR /home/user
