#!/bin/bash
set -e
cd /home/user

chmod 600 /home/user/scripts/deploy.sh && printf "/home/user/scripts/deploy.sh permissions: %s\n" "$(ls -l /home/user/scripts/deploy.sh | awk '{print $1}')" > /home/user/permission_check.log
cat /home/user/permission_check.log
