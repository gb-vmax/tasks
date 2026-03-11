FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create configs directory with configuration files
mkdir -p /home/user/configs

cat > /home/user/configs/app.conf << 'EOF'
[app]
host=localhost
port=8080
debug=false
EOF

cat > /home/user/configs/db.conf << 'EOF'
[database]
host=db.internal
port=5432
name=appdb
user=appuser
EOF

cat > /home/user/configs/nginx.conf << 'EOF'
server {
    listen 80;
    server_name example.com;
    root /var/www/html;
}
EOF

# Create backups directory (empty)
mkdir -p /home/user/backups

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
