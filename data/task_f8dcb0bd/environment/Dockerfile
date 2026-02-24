FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin:$PATH

RUN <<'ENDPOST'
set -e
    apt-get update
    apt-get install -y python3 python3-pip
    pip3 install pytest

    # Create user and home directory if not exists
    useradd -m user || true
    mkdir -p /home/user

    # Set up /home/user/ticket_titles.txt with required contents
    cat > /home/user/ticket_titles.txt <<'EOF'
Cannot connect to VPN
Printer not working
Forgot password
Cannot connect to VPN
Cannot connect to VPN
Printer not working
Software installation request
EOF

    # Set permissions so user can read/write as needed
    chown -R user:user /home/user
    chmod 755 /home/user
    chmod 644 /home/user/ticket_titles.txt
ENDPOST

WORKDIR /home/user
