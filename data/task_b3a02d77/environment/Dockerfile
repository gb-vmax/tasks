FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the config directory and secrets file with overly permissive 0666
mkdir -p /home/user/config
cat > /home/user/config/secrets.env << 'EOF'
DB_PASSWORD=supersecret
API_KEY=abc123
EOF

# Set permissions to 0666 (overly permissive, as required by initial state)
chmod 0666 /home/user/config/secrets.env

# Do NOT create /home/user/audit/ directory — tests assert it does not exist

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
