#!/bin/bash
if lsattr /home/user/report.txt > /tmp/lsattr_output.txt 2>/dev/null && grep -q 'report.txt' /tmp/lsattr_output.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
