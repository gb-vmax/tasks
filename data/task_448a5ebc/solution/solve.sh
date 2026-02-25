#!/bin/bash
set -e
cd /home/user

printf "APP_ENV=production\nDB_HOST=db.prod.company.com\nDB_USER=release_manager\nDB_PASS=Sup3rS3cret!\n" > /home/user/deploy/.env.production
cat > /home/user/deploy/.env.production <<EOF
APP_ENV=production
DB_HOST=db.prod.company.com
DB_USER=release_manager
DB_PASS=Sup3rS3cret!
EOF
set -a; source /home/user/deploy/.env.production; set +a
printf "APP_ENV=%s\nDB_HOST=%s\nDB_USER=%s\nDB_PASS=%s\n" "$APP_ENV" "$DB_HOST" "$DB_USER" "$DB_PASS" > /home/user/deploy/env_check.log
cat /home/user/deploy/env_check.log
