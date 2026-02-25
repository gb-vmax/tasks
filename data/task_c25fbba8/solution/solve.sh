#!/bin/bash
set -e
cd /home/user

find /home/user/app/logs -type f -name "*.log" -mtime +7 -print0 | while IFS= read -r -d '' file; do relpath="${file#/home/user/app/logs/}"; count=$(grep -c 'ERROR' "$file"); echo "${relpath} ERROR_COUNT:${count}"; done > /home/user/error_log_summary.txt
cat /home/user/error_log_summary.txt
