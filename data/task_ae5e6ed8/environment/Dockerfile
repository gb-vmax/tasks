FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install python3 and pip if not already present
    apt-get update
    apt-get install -y python3 python3-pip

    # Install pytest for testing
    pip3 install --no-cache-dir pytest

    # Create user and home directory if not exist
    if ! id user >/dev/null 2>&1; then
        useradd -m -d /home/user user
    fi

    # Ensure /home/user/logs exists with correct permissions
    mkdir -p /home/user/logs
    chown -R user:user /home/user/logs

    # Write the access.log file with the required contents
    cat > /home/user/logs/access.log <<'EOF'
127.0.0.1 - - [15/Feb/2023:09:12:01 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.10 - - [15/Feb/2023:09:15:34 +0000] "GET /about.html HTTP/1.1" 404 512
10.0.0.2 - - [15/Feb/2023:10:05:21 +0000] "GET /contact.html HTTP/1.1" 200 2048
192.168.1.11 - - [15/Feb/2023:10:35:24 +0000] "POST /login HTTP/1.1" 200 512
127.0.0.1 - - [15/Feb/2023:10:50:12 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.10 - - [15/Feb/2023:10:58:07 +0000] "GET /missing.html HTTP/1.1" 404 512
10.0.0.2 - - [15/Feb/2023:11:03:10 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.12 - - [15/Feb/2023:11:33:45 +0000] "GET /index.html HTTP/1.1" 404 1024
192.168.1.11 - - [15/Feb/2023:11:51:19 +0000] "POST /login HTTP/1.1" 200 512
127.0.0.1 - - [15/Feb/2023:11:58:01 +0000] "GET /contact.html HTTP/1.1" 200 2048
EOF

    chown user:user /home/user/logs/access.log
    chmod 644 /home/user/logs/access.log

    # Ensure no other files exist in /home/user/logs
    find /home/user/logs -mindepth 1 ! -name 'access.log' -delete
ENDPOST

WORKDIR /home/user
