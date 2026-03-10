FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create monitoring directory structure
mkdir -p /home/user/monitoring/config

# Set directory permissions
chmod 0755 /home/user/monitoring
chmod 0755 /home/user/monitoring/config

# Create healthcheck.sh with world-writable permissions (0777)
cat > /home/user/monitoring/healthcheck.sh << 'EOF'
#!/bin/bash
curl -s https://example.com/health | grep -q "ok" && echo "UP" || echo "DOWN"
EOF
chmod 0777 /home/user/monitoring/healthcheck.sh

# Create api_credentials.conf with world-readable permissions (0644)
cat > /home/user/monitoring/config/api_credentials.conf << 'EOF'
API_KEY=supersecret123
API_SECRET=topsecretvalue456
ENDPOINT=https://monitoring.example.com/api
EOF
chmod 0644 /home/user/monitoring/config/api_credentials.conf

# Do NOT create audit_report.txt — the agent will create it

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
