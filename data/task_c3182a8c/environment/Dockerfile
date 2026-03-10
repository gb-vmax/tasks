FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the app directory and config file
mkdir -p /home/user/app

cat > /home/user/app/config.ini << 'EOF'
[database]
host = db.internal.example.com
port = 5432
name = appdb
user = appuser
password = s3cr3t

[logging]
level = WARNING
file = /var/log/app/app.log
max_size_mb = 100
rotate = true

[server]
host = 0.0.0.0
port = 8080
max_workers = 8
debug = false
timeout = 30

[cache]
backend = redis
host = cache.internal.example.com
port = 6379
ttl = 300
EOF

# Do NOT create the diagnostics directory — the agent must create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
