FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/configs

cat > /home/user/configs/app.ini << 'EOF'
[database]
host = db.internal.example.com
port = 5432
name = appdb_production

[server]
timeout = 30
debug = false
log_level = info

[auth]
secret_key = s3cr3t!k3y#2024
token_expiry = 3600
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
