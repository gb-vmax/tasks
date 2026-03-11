#!/bin/bash
set -e
cd /home/user

cat /home/user/apps/staging/.env
sed -i 's|DB_HOST=db-prod.internal.company.com|DB_HOST=db-staging.internal.company.com|' /home/user/apps/staging/.env && sed -i 's|API_KEY=sk-old-key-deprecated-111111|API_KEY=sk-staging-9f2a1c4e8b3d7f6a|' /home/user/apps/staging/.env
cat /home/user/apps/staging/.env
printf 'DB_HOST=db-staging.internal.company.com\nDB_PORT=5432\nAPI_KEY=sk-staging-9f2a1c4e8b3d7f6a\nAPP_ENV=staging\n' > /home/user/apps/staging/env_summary.txt
cat /home/user/apps/staging/env_summary.txt
wc -l /home/user/apps/staging/env_summary.txt && cat -A /home/user/apps/staging/env_summary.txt
