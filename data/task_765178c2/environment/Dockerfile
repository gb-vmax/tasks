FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create deployment directory and files
mkdir -p /home/user/deployments/app-v2.3.1

cat > /home/user/deployments/app-v2.3.1/config.yml << 'EOF'
environment: production
port: 8080
log_level: info
database_url: postgres://db.internal:5432/appdb
EOF

cat > /home/user/deployments/app-v2.3.1/run.sh << 'EOF'
#!/bin/bash
echo "Starting app-v2.3.1"
exec ./app --config config.yml
EOF

cat > /home/user/deployments/app-v2.3.1/app << 'EOF'
BINARY_PLACEHOLDER_v2.3.1
EOF

# Create empty backups directory
mkdir -p /home/user/backups

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
