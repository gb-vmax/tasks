FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install required packages: python3-pip for pytest, plus awk and sed (already in base, but ensure)
    apt-get update
    apt-get install -y python3-pip gawk sed
    pip3 install --no-cache-dir pytest

    # Create user and home directory if not already present
    useradd -m user || true

    # Create logs and diagnostics directories
    mkdir -p /home/user/logs
    mkdir -p /home/user/diagnostics

    # Set permissions: user owns everything in their home
    chown -R user:user /home/user

    # Ensure diagnostics directory is writable by user
    chmod 700 /home/user/diagnostics

    # Write the initial access.log with correct UNIX (LF) line endings
    cat > /home/user/logs/access.log <<'EOF'
192.168.1.10 - - [01/Apr/2024:10:01:23 +0000] "GET /index.html HTTP/1.1" 200 532
192.168.1.11 - - [01/Apr/2024:10:02:17 +0000] "GET /logo.png HTTP/1.1" 404 102
10.0.0.5 - - [01/Apr/2024:10:03:11 +0000] "POST /submit HTTP/1.1" 500 12
192.168.1.10 - - [01/Apr/2024:10:05:44 +0000] "GET /contact HTTP/1.1" 404 102
10.0.0.7 - - [01/Apr/2024:10:06:50 +0000] "GET /about HTTP/1.1" 200 198
192.168.1.20 - - [01/Apr/2024:10:08:02 +0000] "GET /index.html HTTP/1.1" 301 68
192.168.1.11 - - [01/Apr/2024:10:09:33 +0000] "GET /missing HTTP/1.1" 404 102
10.0.0.5 - - [01/Apr/2024:10:12:18 +0000] "GET /error HTTP/1.1" 500 12
EOF

    # Set permissions: access.log should be readable/writable by user
    chown user:user /home/user/logs/access.log
    chmod 600 /home/user/logs/access.log
ENDPOST

WORKDIR /home/user
