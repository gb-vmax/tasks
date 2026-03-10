#!/bin/bash
set -e
cd /home/user

{
  echo "Disk Usage Report: /home/user/net_data"
  echo ""
  du -sh /home/user/net_data/*/ 2>/dev/null | sort -rh
  echo ""
  echo "Total: $(du -sh /home/user/net_data | cut -f1)"
} > /home/user/disk_report.txt
cat /home/user/disk_report.txt
{
  echo "Disk Usage Report: /home/user/net_data"
  echo ""
  du -sh /home/user/net_data/*/ 2>/dev/null | sed 's|/$||' | sort -rh
  echo ""
  echo "Total: $(du -sh /home/user/net_data | cut -f1)"
} > /home/user/disk_report.txt
cat /home/user/disk_report.txt
