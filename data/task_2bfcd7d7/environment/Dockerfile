FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the configs directory
mkdir -p /home/user/configs

# Create the registry.json file with the expected content
cat > /home/user/configs/registry.json << 'EOF'
[
  {"service": "auth-service", "env": "production", "last_modified": "2024-11-01", "enabled": true, "version": "2.3.1"},
  {"service": "billing-api", "env": "staging", "last_modified": "2024-10-15", "enabled": false, "version": "1.0.4"},
  {"service": "cache-manager", "env": "development", "last_modified": "2024-11-20", "enabled": true, "version": "0.9.2"},
  {"service": "data-pipeline", "env": "production", "last_modified": "2024-09-30", "enabled": true, "version": "3.1.0"},
  {"service": "email-worker", "env": "staging", "last_modified": "2024-11-05", "enabled": false, "version": "1.2.0"},
  {"service": "feature-flags", "env": "production", "last_modified": "2024-10-22", "enabled": true, "version": "1.5.3"}
]
EOF

# Ensure correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
