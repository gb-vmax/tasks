FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create configs directory
mkdir -p /home/user/configs

# Create service.yaml
cat > /home/user/configs/service.yaml << 'EOF'
service:
  name: auth-service
  version: 2.4.1
  environment: production

database:
  host: db-primary.internal
  port: 5432
  pool_size: 10
  ssl: true
EOF

# Create app.toml
cat > /home/user/configs/app.toml << 'EOF'
[server]
host = "0.0.0.0"
port = 8080
timeout = 30
workers = 4

[logging]
level = "warn"
file = "/var/log/app/app.log"
format = "json"

[cache]
enabled = true
ttl = 300
EOF

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
