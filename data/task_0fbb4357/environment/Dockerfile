FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create deploy directory structure
mkdir -p /home/user/deploy/config
mkdir -p /home/user/deploy/logs

# Create start.sh with initial permissions 0777
cat > /home/user/deploy/start.sh << 'EOF'
#!/bin/bash
echo 'Starting app'
EOF
chmod 0777 /home/user/deploy/start.sh

# Create config/db.conf with initial permissions 0644
cat > /home/user/deploy/config/db.conf << 'EOF'
host=localhost
password=s3cr3t
EOF
chmod 0644 /home/user/deploy/config/db.conf

# Create config/app.conf with initial permissions 0666
cat > /home/user/deploy/config/app.conf << 'EOF'
debug=false
port=8080
EOF
chmod 0666 /home/user/deploy/config/app.conf

# Set logs/ directory permissions to 0777
chmod 0777 /home/user/deploy/logs

# Do NOT create security_audit.txt — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
