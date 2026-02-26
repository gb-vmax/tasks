FROM endless-base:latest

RUN <<'ENDPOST'
set -e

    # Install Python3 and pip (needed for pytest)
    apt-get update
    apt-get install -y python3 python3-pip

    # Install pytest for testing
    pip3 install pytest

    # Create user and home directory
    useradd -m user || true

    # Set up directory structure
    mkdir -p /home/user/source_configs
    mkdir -p /home/user/hardened_configs

    # Set up the sample source .conf files with correct content and permissions
    cat > /home/user/source_configs/db.conf <<EOF
db_user=admin
db_pass=secret
EOF

    cat > /home/user/source_configs/web.conf <<EOF
server_name=example.com
listen=80
EOF

    cat > /home/user/source_configs/bad.conf <<EOF
config_break
EOF

    # Set ownership and permissions for user
    chown -R user:user /home/user/source_configs /home/user/hardened_configs
    chmod 700 /home/user/source_configs
    chmod 700 /home/user/hardened_configs

    # Ensure all sample files are user-readable
    chmod 600 /home/user/source_configs/*.conf
ENDPOST

WORKDIR /home/user
