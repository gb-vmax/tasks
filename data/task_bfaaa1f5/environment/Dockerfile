FROM endless-deps-41ffca929b95:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the app directory
mkdir -p /home/user/app

# Create the config.env file with the initial content
cat > /home/user/app/config.env << 'EOF'
APP_ENV=production
DB_HOST=db.internal.example.com
DB_PORT=5432
API_KEY=a3f8c2e1b7d94f0612345678abcdef90
LOG_LEVEL=warn
MAX_CONNECTIONS=50
EOF

# Create the rotation_log.txt with the two existing entries
cat > /home/user/app/rotation_log.txt << 'EOF'
ROTATED DB_PASSWORD on 2024-11-01 old=hunter24 new=9f2a3b1c
ROTATED API_KEY on 2024-12-15 old=ccf01234 new=ab987654
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
