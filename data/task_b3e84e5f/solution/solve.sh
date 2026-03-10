#!/bin/bash
set -e
cd /home/user

ls /home/user/appdata
HOSTNAME=$(hostname)
TOTAL=$(du -sk /home/user/appdata | awk '{print $1}')
AVAILABLE=$(df -k /home/user/appdata | awk 'NR==2 {print $4}')

{
  echo "=== DISK USAGE REPORT ==="
  echo "Generated: $HOSTNAME"
  echo ""
  echo "Top directories by size:"
  du -sk /home/user/appdata/*/ 2>/dev/null | sort -rn | head -5 | awk '{printf "  %sK  %s\n", $1, $2}'
  echo ""
  echo "Total usage: ${TOTAL}K"
  echo "Available: ${AVAILABLE}K"
} > /home/user/disk_report.txt
cat /home/user/disk_report.txt
cat -A /home/user/disk_report.txt | head -10
HOSTNAME=$(hostname)
TOTAL=$(du -sk /home/user/appdata | awk '{print $1}')
AVAILABLE=$(df -k /home/user/appdata | awk 'NR==2 {print $4}')

{
  echo "=== DISK USAGE REPORT ==="
  echo "Generated: $HOSTNAME"
  echo ""
  echo "Top directories by size:"
  du -sk /home/user/appdata/*/ 2>/dev/null | sort -rn | head -5 | awk '{
    path = $2
    sub(/\/$/, "", path)
    printf "  %sK  %s\n", $1, path
  }'
  echo ""
  echo "Total usage: ${TOTAL}K"
  echo "Available: ${AVAILABLE}K"
} > /home/user/disk_report.txt
cat /home/user/disk_report.txt
cat -A /home/user/disk_report.txt
