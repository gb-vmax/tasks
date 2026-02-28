#!/bin/bash
set -e
if [ ! -f /home/user/report_link.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
orig_inode=$(stat -c%i /home/user/report.txt)
link_inode=$(stat -c%i /home/user/report_link.txt)
if [ "$orig_inode" = "$link_inode" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
