FROM ubuntu:22.04

ENV PATH=/home/user/.local/bin:$PATH

RUN <<'ENDPOST'
set -eux

    # Create user and home directory if not present
    if ! id user >/dev/null 2>&1; then
        useradd -m -s /bin/bash user
    fi

    mkdir -p /home/user/security
    chown user:user /home/user/security
    chmod 700 /home/user/security

    # Create the access.log file with the specified content
    cat > /home/user/security/access.log <<'EOF'
2024-06-05 12:21:11 - user:alice - action:login - status:success - ip:192.168.1.15
2024-06-05 12:22:18 - user:bob - action:failed - status:invalid_password - ip:192.168.1.33
2024-06-05 12:25:41 - user:charlie - action:login - status:success - ip:10.0.0.5
2024-06-05 12:26:00 - user:alice - action:token_refresh - status:success - ip:192.168.1.15
2024-06-05 12:27:14 - user:dave - action:logout - status:success - ip:172.16.0.18
2024-06-05 12:28:01 - user:bob - action:login - status:success - ip:192.168.1.33
2024-06-05 12:28:17 - user:alice - action:failed - status:invalid_password - ip:192.168.1.15
2024-06-05 12:29:05 - user:charlie - action:token_refresh - status:success - ip:10.0.0.5
2024-06-05 12:30:11 - user:alice - action:login - status:success - ip:192.168.1.15
EOF

    chown user:user /home/user/security/access.log
    chmod 600 /home/user/security/access.log

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip python3-setuptools
    pip3 install --no-cache-dir pytest
ENDPOST

WORKDIR /home/user
