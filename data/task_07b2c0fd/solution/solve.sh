#!/bin/bash
set -e
cd /home/user

ls /home/user/services/
stat --format="%n %a" /home/user/services/README.md /home/user/services/api_secret.key /home/user/services/app_config.yaml /home/user/services/auth_token.txt /home/user/services/db_credentials.env /home/user/services/nginx_config.conf
chmod 600 /home/user/services/api_secret.key /home/user/services/auth_token.txt /home/user/services/db_credentials.env && chmod 640 /home/user/services/app_config.yaml /home/user/services/nginx_config.conf && chmod 644 /home/user/services/README.md
cat > /home/user/services/audit_report.txt << 'EOF'
PERMISSION AUDIT REPORT
=======================
FILE: README.md
  BEFORE: 777
  AFTER: 644
FILE: api_secret.key
  BEFORE: 777
  AFTER: 600
FILE: app_config.yaml
  BEFORE: 777
  AFTER: 640
FILE: auth_token.txt
  BEFORE: 755
  AFTER: 600
FILE: db_credentials.env
  BEFORE: 777
  AFTER: 600
FILE: nginx_config.conf
  BEFORE: 755
  AFTER: 640
=======================
TOTAL FILES REMEDIATED: 6
EOF
stat --format="%n %a" /home/user/services/README.md /home/user/services/api_secret.key /home/user/services/app_config.yaml /home/user/services/auth_token.txt /home/user/services/db_credentials.env /home/user/services/nginx_config.conf /home/user/services/audit_report.txt
cat /home/user/services/audit_report.txt
