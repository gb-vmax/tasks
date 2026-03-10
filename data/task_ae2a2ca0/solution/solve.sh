#!/bin/bash
set -e
cd /home/user

ls /home/user/webapp
find /home/user/webapp -type f -perm -o+w | sort
mkdir -p /home/user/diagnostics
DATE=$(date +%Y-%m-%d)
FILES=$(find /home/user/webapp -type f -perm -o+w | sort)
COUNT=$(echo "$FILES" | grep -c .)

{
  echo "=== WORLD-WRITABLE FILES SCAN ==="
  echo "Directory: /home/user/webapp"
  echo "Date: $DATE"
  echo ""
  echo "Files found:"
  echo "$FILES"
  echo ""
  echo "Total: $COUNT file(s) found"
} > /home/user/diagnostics/security_scan.txt
cat /home/user/diagnostics/security_scan.txt
