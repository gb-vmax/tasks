#!/bin/bash
if [ -f /home/user/archive/report_link.txt ] && [ -f /home/user/reports/2020/report.txt ]; then
  if [ "$(cat /home/user/archive/report_link.txt)" = "Annual Report 2020" ]; then
    orig_inode=$(stat -c %i /home/user/reports/2020/report.txt)
    link_inode=$(stat -c %i /home/user/archive/report_link.txt)
    if [ "$orig_inode" = "$link_inode" ]; then
      echo 1 > /logs/verifier/reward.txt
      exit 0
    fi
  fi
fi
echo 0 > /logs/verifier/reward.txt
