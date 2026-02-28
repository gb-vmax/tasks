#!/bin/bash
if [ -f /home/user/new_report.txt ] && [ ! -f /home/user/old_report.txt ] && grep -q "Q2 sales data" /home/user/new_report.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
