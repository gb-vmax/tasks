#!/bin/bash
set -e
cd /home/user

head -20 /home/user/logs/app.log
grep 'ERROR' /home/user/logs/app.log > /home/user/logs/errors_only.log
count=$(wc -l < /home/user/logs/errors_only.log) && printf "Total ERROR lines: %s\n" "$count" > /home/user/logs/error_summary.txt
cat /home/user/logs/errors_only.log && echo "---" && cat /home/user/logs/error_summary.txt
