#!/bin/bash
set -e
cd /home/user

usermod -aG finops analyst
chown -R :finops /home/user/finops/reports
chmod 750 /home/user/finops/reports
find /home/user/finops/reports -maxdepth 1 -type f -exec chmod 640 {} +
ls -la /home/user/finops/reports && echo "---" && groups analyst
