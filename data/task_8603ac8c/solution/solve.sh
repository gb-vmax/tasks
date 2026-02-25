#!/bin/bash
set -e
cd /home/user

grep -iE 'authentication failed|invalid password' /home/user/server/app.log > /home/user/server/auth_failure.log
echo "Total failures: $(wc -l < /home/user/server/auth_failure.log)" > /home/user/server/auth_summary.txt
