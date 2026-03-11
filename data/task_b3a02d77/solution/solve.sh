#!/bin/bash
set -e
cd /home/user

chmod 600 /home/user/config/secrets.env && mkdir -p /home/user/audit && echo 'ENFORCED 600 /home/user/config/secrets.env' > /home/user/audit/permissions.log
stat -c "%a" /home/user/config/secrets.env && cat /home/user/audit/permissions.log
