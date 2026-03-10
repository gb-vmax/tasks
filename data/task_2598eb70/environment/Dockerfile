FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create directory structure
mkdir -p /home/user/services/gateway
mkdir -p /home/user/services/broker

# Create the initial YAML config file
cat > /home/user/services/gateway/config.yaml << 'EOF'
service:
  name: api-gateway
  replicas: 2
  image:
    repository: myregistry/api-gateway
    tag: v2.4.0
  resources:
    limits:
      memory: 512Mi
      cpu: "500m"
    requests:
      memory: 256Mi
      cpu: "250m"
  port: 8080
  env: production
EOF

# Create the initial TOML config file
cat > /home/user/services/broker/config.toml << 'EOF'
[service]
name = "message-broker"
version = "1.3.0"
env = "production"

[pool]
max_connections = 50
min_connections = 5
timeout_seconds = 10
idle_timeout = 300

[telemetry]
enabled = false
endpoint = "http://metrics.internal:9090"
interval_seconds = 15
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
