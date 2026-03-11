#!/bin/bash
set -e
cd /home/user

cat /home/user/logs/nginx-service.log
grep '\[ERROR\]' /home/user/logs/nginx-service.log > /home/user/logs/errors_only.log
echo "Total errors: $(grep -c '\[ERROR\]' /home/user/logs/nginx-service.log)" > /home/user/logs/error_summary.txt
cat /home/user/logs/errors_only.log && echo "---" && cat /home/user/logs/error_summary.txt
