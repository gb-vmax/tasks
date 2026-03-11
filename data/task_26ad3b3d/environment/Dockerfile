FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/audit/configs

cat > /home/user/audit/configs/webserver.ini << 'EOF'
[server]
ssl_enabled = true
max_connections = 250
log_level = debug
timeout_seconds = 20

[security]
auth_required = true
ssl_enabled = true
EOF

cat > /home/user/audit/configs/database.ini << 'EOF'
[connection]
ssl_enabled = true
max_connections = 50
timeout_seconds = 60

[auth]
auth_required = false
log_level = error
EOF

cat > /home/user/audit/configs/mailrelay.ini << 'EOF'
[relay]
ssl_enabled = true
max_connections = 10
log_level = warn
timeout_seconds = 25

[access]
auth_required = true
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
