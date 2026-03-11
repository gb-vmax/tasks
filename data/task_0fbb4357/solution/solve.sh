#!/bin/bash
set -e
cd /home/user

ls -la /home/user/deploy/ && ls -la /home/user/deploy/config/ && ls -la /home/user/deploy/logs/
chmod 750 /home/user/deploy/start.sh && chmod 600 /home/user/deploy/config/db.conf && chmod 640 /home/user/deploy/config/app.conf && chmod 750 /home/user/deploy/logs/
cat > /home/user/deploy/security_audit.txt << 'EOF'
DEPLOYMENT SECURITY AUDIT
=========================
start.sh: -rwxr-x---
config/db.conf: -rw-------
config/app.conf: -rw-r-----
logs/: drwxr-x---
STATUS: SECURED
EOF
ls -la /home/user/deploy/start.sh /home/user/deploy/config/db.conf /home/user/deploy/config/app.conf /home/user/deploy/logs/ && cat /home/user/deploy/security_audit.txt
