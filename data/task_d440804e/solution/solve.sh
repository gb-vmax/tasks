#!/bin/bash
set -e
cd /home/user

cat /home/user/app/config.env
sed -i 's/^API_KEY=.*/API_KEY=sk-prod-9x2mK7vLqR4nYpW3hJtZ8cBdE1fG6aU0/' /home/user/app/config.env
echo 'ROTATED API_KEY old=sk-prod-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX new=sk-prod-9x2mK7vLqR4nYpW3hJtZ8cBdE1fG6aU0 by=security-engineer' >> /home/user/security/audit.log
cat /home/user/app/config.env && echo "---" && tail -5 /home/user/security/audit.log
