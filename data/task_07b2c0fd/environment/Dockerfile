FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

SERVICES_DIR="/home/user/services"
mkdir -p "$SERVICES_DIR"

# Create files with specified contents and permissions

# db_credentials.env — permissions 777
cat > "$SERVICES_DIR/db_credentials.env" << 'EOF'
DB_PASSWORD=supersecret
EOF
chmod 777 "$SERVICES_DIR/db_credentials.env"

# api_secret.key — permissions 777
cat > "$SERVICES_DIR/api_secret.key" << 'EOF'
API_SECRET=abc123xyz
EOF
chmod 777 "$SERVICES_DIR/api_secret.key"

# auth_token.txt — permissions 755
cat > "$SERVICES_DIR/auth_token.txt" << 'EOF'
TOKEN=eyJhbGci
EOF
chmod 755 "$SERVICES_DIR/auth_token.txt"

# app_config.yaml — permissions 777
cat > "$SERVICES_DIR/app_config.yaml" << 'EOF'
port: 8080
host: localhost
EOF
chmod 777 "$SERVICES_DIR/app_config.yaml"

# nginx_config.conf — permissions 755
cat > "$SERVICES_DIR/nginx_config.conf" << 'EOF'
worker_processes 1;
EOF
chmod 755 "$SERVICES_DIR/nginx_config.conf"

# README.md — permissions 777
cat > "$SERVICES_DIR/README.md" << 'EOF'
# Services
EOF
chmod 777 "$SERVICES_DIR/README.md"

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
