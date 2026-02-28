#!/bin/bash
if [ -f /home/user/project/final_report.txt ] && \
   [ "$(stat -c%i /home/user/project/final_report.txt)" = "$(stat -c%i /home/user/reports/draft_report.txt)" ] && \
   cmp -s /home/user/project/final_report.txt /home/user/reports/draft_report.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
