FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the staging app directory
mkdir -p /home/user/apps/staging

# Create the initial .env file with incorrect values (as the agent will find it)
cat > /home/user/apps/staging/.env << 'EOF'
APP_ENV=staging
APP_PORT=8080
DB_HOST=db-prod.internal.company.com
DB_PORT=5432
DB_USER=staginguser
DB_PASSWORD=hunter2
API_KEY=sk-old-key-deprecated-111111
LOG_LEVEL=debug
EOF

# Do NOT create env_summary.txt — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
