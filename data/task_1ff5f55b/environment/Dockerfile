FROM ubuntu:22.04

RUN <<'ENDPOST'
set -eux

    # Create user and home directory if not already present
    if ! id user >/dev/null 2>&1; then
        useradd -m -s /bin/bash user
    fi

    # Create /home/user/tools directory
    mkdir -p /home/user/tools
    chown user:user /home/user/tools

    # Create /home/user/tools/ping_test.sh with correct content and permissions
    cat >/home/user/tools/ping_test.sh <<'EOF'
#!/bin/bash
ping -c 3 8.8.8.8 > /home/user/tools/ping_output.log
EOF
    chown user:user /home/user/tools/ping_test.sh
    chmod 755 /home/user/tools/ping_test.sh

    # Create an empty /home/user/tools/ping_output.log file
    touch /home/user/tools/ping_output.log
    chown user:user /home/user/tools/ping_output.log
    chmod 644 /home/user/tools/ping_output.log

    # Install pip and pytest (and dependencies)
    apt-get update
    apt-get install -y python3-pip python3-setuptools python3-wheel
    pip3 install --no-cache-dir pytest
ENDPOST

WORKDIR /home/user
