FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the app directory and .env file
mkdir -p /home/user/app

cat > /home/user/app/.env << 'EOF'
APP_ENV=production
APP_PORT=8080
DB_HOST=db.internal
DB_PASSWORD=supersecret123
LOG_LEVEL=info
SECRET_KEY=abc123xyz789
EOF

# Do NOT create /home/user/diagnostics — the agent must create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
