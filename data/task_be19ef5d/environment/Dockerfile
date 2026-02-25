FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest

    # Create user and logs directory
    mkdir -p /home/user/logs

    # Create sample access log with required entries
    cat > /home/user/logs/webserver_access.log <<EOF
127.0.0.1 - - [10/Jun/2024:10:15:32 +0000] "GET /index.html HTTP/1.1" 200 1024
127.0.0.1 - - [10/Jun/2024:10:16:03 +0000] "GET /nonexistent.jpg HTTP/1.1" 404 512
127.0.0.1 - - [10/Jun/2024:10:16:45 +0000] "POST /api/v1/users HTTP/1.1" 201 2048
127.0.0.1 - - [10/Jun/2024:10:17:10 +0000] "GET /not_found.html HTTP/1.1" 404 256
127.0.0.1 - - [10/Jun/2024:10:17:45 +0000] "GET /favicon.ico HTTP/1.1" 200 150
EOF

    # Set ownership and permissions so that /home/user/logs is user-writeable
    chmod 755 /home/user
    chmod 777 /home/user/logs
    chmod 666 /home/user/logs/webserver_access.log
ENDPOST

WORKDIR /home/user
