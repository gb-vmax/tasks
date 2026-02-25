FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

install -d -o user -g user /home/user/server_config

cat > /home/user/server_config/monitoring.ini <<'EOF'
[general]
global_interval=300
notify_admin=yes

[server_web01]
hostname=web01
ip=192.168.10.10
enabled=TRUE
interval=60

[server_db01]
hostname=db01
ip=192.168.10.20
enabled=true
interval=120

[server_lb]
hostname=lb01
ip=192.168.10.30
enabled=FALSE
interval=90

[server_cache]
hostname=cache01
ip=192.168.10.40
enabled=True
interval=45

[backup]
location=/mnt/backup
server=server_db01
EOF

chown user:user /home/user/server_config/monitoring.ini
chmod 644 /home/user/server_config/monitoring.ini

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
