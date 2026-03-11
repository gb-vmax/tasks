FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/provisioning

cat > /home/user/provisioning/server.conf.tmpl << 'EOF'
# Server Configuration
hostname = {{HOSTNAME}}
bind_address = {{IP_ADDRESS}}
environment = {{ENVIRONMENT}}

[connection]
max_connections = {{MAX_CONNECTIONS}}
timeout = {{TIMEOUT_SECONDS}}

[logging]
log_file = /var/log/{{HOSTNAME}}/app.log
log_level = info

[tags]
env = {{ENVIRONMENT}}
host = {{HOSTNAME}}
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
