#!/bin/bash
set -e
cd /home/user

cat >> /home/user/.bashrc << 'EOF'
# App deployment config
export APP_ENV=production
export APP_PORT=8443
export APP_LOG_LEVEL=warn
export APP_MAX_WORKERS=8
export APP_DATA_DIR=/var/app/data
EOF
tail -10 /home/user/.bashrc
perl -i -0pe 's/\n+$/\n/' /home/user/.bashrc
tail -10 /home/user/.bashrc
cat -A /home/user/.bashrc | tail -10
source /home/user/.bashrc && env | grep "^APP_" | sort > /home/user/env_check.txt
cat /home/user/env_check.txt
cat -A /home/user/env_check.txt
