FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/deploy

cat > /home/user/deploy/.env.production <<EOF
APP_ENV=production
DB_HOST=db.prod.company.com
DB_USER=release_manager
DB_PASS=Sup3rS3cret!
EOF

cat > /home/user/deploy/env_check.log <<EOF
APP_ENV=production
DB_HOST=db.prod.company.com
DB_USER=release_manager
DB_PASS=Sup3rS3cret!
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
