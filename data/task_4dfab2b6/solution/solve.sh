#!/bin/bash
set -e
cd /home/user

printf 'PGUSER=db_backup_user\nPGPASSWORD=S3cr3tP@ssw0rd2024' > /home/user/db_backup/.env
set -a; source /home/user/db_backup/.env; set +a; echo "$PGUSER"; echo "$PGPASSWORD"
printf 'PGUSER=db_backup_user\nPGPASSWORD=S3cr3tP@ssw0rd2024' > /home/user/db_backup/backup_env_check.log
cat -A /home/user/db_backup/backup_env_check.log
