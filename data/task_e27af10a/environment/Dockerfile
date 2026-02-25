FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin:$PATH

RUN <<'ENDPOST'
set -e

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest

    # Create the user and config directories
    mkdir -p /home/user/config

    # Create the settings.cfg file with the specified content
    cat > /home/user/config/settings.cfg <<EOF
user=alice
timeout=unchanged
theme=dark
autosave=unchanged
language=en
EOF

    # Set permissions so the agent (non-root) can read/write as needed
    chmod 755 /home/user
    chmod 755 /home/user/config
    chmod 644 /home/user/config/settings.cfg
ENDPOST

WORKDIR /home/user
