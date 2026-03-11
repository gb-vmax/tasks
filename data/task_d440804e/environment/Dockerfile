FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create directories
mkdir -p /home/user/app
mkdir -p /home/user/security

# Create config.env with original API key
cat > /home/user/app/config.env << 'EOF'
APP_ENV=production
DB_HOST=db.internal.example.com
DB_PORT=5432
API_KEY=sk-prod-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
LOG_LEVEL=warn
TIMEOUT=30
EOF

# Create audit.log with two existing entries (no trailing newline beyond last line)
printf 'ROTATED DB_PASSWORD old=hunter2 new=xK9#mPqL2v by=security-engineer\nROTATED S3_SECRET old=wJbN3rTy7z new=vH6kD1sA4f by=security-engineer\n' > /home/user/security/audit.log

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
