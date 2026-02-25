FROM ubuntu:22.04

RUN <<'ENDPOST'
apt-get update
    apt-get install -y python3-pip
    pip3 install pytest

    # Create the directory structure with correct permissions
    mkdir -p /home/user/server_configs
    chown -R 1000:1000 /home/user
    chmod 755 /home/user
    chmod 755 /home/user/server_configs

    # Create the prod_server.ini file with exact required contents
    cat > /home/user/server_configs/prod_server.ini << 'EOF'
[General]
log_level=INFO
admin_email=admin@example.com

[Database]
host=db.production.example.com
port=5432
user=produser
password=secureP@ssw0rd

[Cache]
enabled=true
size=256M
EOF

    # Ensure permissions are correct for the file and directory
    chown 1000:1000 /home/user/server_configs/prod_server.ini
    chmod 644 /home/user/server_configs/prod_server.ini
ENDPOST

WORKDIR /home/user
