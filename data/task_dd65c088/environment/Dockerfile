FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install python3 and pip
    apt-get update
    apt-get install -y python3 python3-pip

    # Install pytest
    pip3 install --no-cache-dir pytest

    # Create user and home directory if not exists
    if ! id -u user >/dev/null 2>&1; then
        useradd -m -s /bin/bash user
    fi

    # Create migration directory and set permissions
    install -d -m 0777 /home/user/migration

    # Create migration.log with specified contents
    cat > /home/user/migration/migration.log <<'EOF'
[2024-06-01 10:00:00] database: SUCCESS
[2024-06-01 10:05:10] cache: FAILURE
[2024-06-01 10:10:15] frontend: SUCCESS
[2024-06-01 10:12:20] backend: SUCCESS
[2024-06-01 10:14:55] worker: FAILURE
EOF

    # Set permissions so non-root user can write in migration dir and log file
    chmod 0777 /home/user/migration
    chmod 0666 /home/user/migration/migration.log
ENDPOST

WORKDIR /home/user
