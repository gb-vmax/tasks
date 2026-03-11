#!/bin/bash
set -e
cd /home/user

cat /home/user/configs/app.ini
printf 'export TEST_DATABASE_HOST=db.internal.example.com\nexport TEST_DATABASE_PORT=5432\nexport TEST_DATABASE_NAME=appdb_production\nexport TEST_SERVER_TIMEOUT=30\nexport TEST_SERVER_DEBUG=false\nexport TEST_AUTH_SECRET_KEY=s3cr3t!k3y#2024\n' > /home/user/configs/test_env.sh && chmod 755 /home/user/configs/test_env.sh
cat /home/user/configs/test_env.sh && ls -l /home/user/configs/test_env.sh
