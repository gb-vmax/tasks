FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin:$PATH

RUN <<'ENDPOST'
set -e

    # Create user and home directory if not already present
    useradd -m user || true

    # Create required directories for the task
    mkdir -p /home/user/configs

    # Create the initial auth_config.ini file with the given content
    cat > /home/user/configs/auth_config.ini << 'EOF'
[ssh]
alice = allowed
bob = denied
felix = allowed

[ftp]
carol = allowed

[http]
bob = allowed
diana = denied
EOF

    # Set ownership and permissions to ensure 'user' can read/write as needed
    chown -R user:user /home/user/configs
    chmod 700 /home/user/configs
    chmod 600 /home/user/configs/auth_config.ini

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest
ENDPOST

WORKDIR /home/user
