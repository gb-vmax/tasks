FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the appdata directory and files with initial 644 permissions
mkdir -p /home/user/appdata
mkdir -p /home/user/backups

# Create db.conf with database credentials
cat > /home/user/appdata/db.conf << 'EOF'
host=localhost
user=admin
password=supersecret123
EOF

# Create api_keys.conf with API secrets
cat > /home/user/appdata/api_keys.conf << 'EOF'
STRIPE_KEY=sk_live_abc123
SENDGRID_KEY=SG.xyz987
EOF

# Create app.log with application log entries
cat > /home/user/appdata/app.log << 'EOF'
2024-01-10 08:00:01 INFO Application started
2024-01-10 08:00:05 INFO Listening on port 8080
EOF

# Set initial permissions to 644 (world-readable) as specified
chmod 644 /home/user/appdata/db.conf
chmod 644 /home/user/appdata/api_keys.conf
chmod 644 /home/user/appdata/app.log

# Ensure backups directory is empty (no output files created)
# The agent will create files there

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
