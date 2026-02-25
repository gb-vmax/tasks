FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest

    # Create the /home/user/appconfig directory with proper permissions
    mkdir -p /home/user/appconfig
    chown root:root /home/user/appconfig
    chmod 755 /home/user/appconfig

    # Create the settings.ini file with specified contents and permissions
    cat > /home/user/appconfig/settings.ini <<'EOF'
[network]
hostname = app-host
port = 443
ssl_enabled = true

[user]
username = admin
email = admin@example.com

[database]
db_name = appdb
db_port = 5432
timeout = 60

[network]
proxy = enabled
proxy_port = 3128
EOF

    # Ensure the file is user-writable (owner write permission)
    chmod 644 /home/user/appconfig/settings.ini
ENDPOST

WORKDIR /home/user
