FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the configs directory
mkdir -p /home/user/configs

# Create the v1 config file
cat > /home/user/configs/app.conf.v1 << 'EOF'
host=localhost
port=8080
debug=true
max_connections=100
timeout=30
log_level=info
EOF

# Create the v2 config file
cat > /home/user/configs/app.conf.v2 << 'EOF'
host=localhost
port=9090
debug=false
max_connections=100
timeout=60
log_level=warn
workers=4
EOF

# Do NOT create changes.txt — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
