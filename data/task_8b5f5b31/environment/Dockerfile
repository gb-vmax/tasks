FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the infra/configs directory structure
mkdir -p /home/user/infra/configs

# Create nginx.conf
cat > /home/user/infra/configs/nginx.conf << 'EOF'
worker_processes 4;
events { worker_connections 1024; }
http {
    server {
        listen 80;
        server_name example.com;
    }
}
EOF

# Create db.env
cat > /home/user/infra/configs/db.env << 'EOF'
DB_HOST=10.0.1.5
DB_PORT=5432
DB_NAME=appdb
DB_USER=appuser
EOF

# Create haproxy.cfg
cat > /home/user/infra/configs/haproxy.cfg << 'EOF'
global
    log /dev/log local0
defaults
    timeout connect 5s
    timeout client 30s
    timeout server 30s
EOF

# Do NOT create the backups directory — the agent must create it
# Do NOT create any archive or checksum files

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
