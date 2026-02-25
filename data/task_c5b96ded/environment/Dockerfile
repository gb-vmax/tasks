FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

mkdir -p /home/user/system/config

cat > /home/user/system/config/settings.conf <<'EOF'
# System network configuration
net_mode=auto   # automatic mode enabled
max_connections=10
net_timeout=30
#net_debug=true
device_id=serv01
net_interface=eth0    # main interface
# End of config
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
