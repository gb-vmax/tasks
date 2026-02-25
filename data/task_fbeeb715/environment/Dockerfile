FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest

    # Create user and home directory if needed
    if ! id user >/dev/null 2>&1; then
        useradd -m -s /bin/bash user
    fi

    # Ensure /home/user/creds exists and is owned by user
    install -d -m 700 -o user -g user /home/user/creds

    # Create /home/user/creds/users.csv with the specified content
    cat > /home/user/creds/users.csv <<EOF
user_id,username,email,api_key
1,alice,alice@example.com,oldkey-123
2,bob,bob@example.com,oldkey-456
3,charlie,charlie@example.com,oldkey-789
EOF

    # Create /home/user/creds/new_keys.txt with the specified content
    cat > /home/user/creds/new_keys.txt <<EOF
newkey-ab1
newkey-cd2
newkey-ef3
EOF

    # Set ownership and permissions for files
    chown user:user /home/user/creds/users.csv /home/user/creds/new_keys.txt
    chmod 600 /home/user/creds/users.csv /home/user/creds/new_keys.txt
ENDPOST

WORKDIR /home/user
