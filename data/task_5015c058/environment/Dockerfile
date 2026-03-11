FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the configs directory
mkdir -p /home/user/configs

# Create the initial app.conf file with the expected content
cat > /home/user/configs/app.conf << 'EOF'
# Application Configuration
host=localhost
port=8080
log_level=info
max_connections=100
timeout=30
debug_mode=false
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
