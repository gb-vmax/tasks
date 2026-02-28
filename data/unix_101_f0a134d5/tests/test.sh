#!/bin/bash
if [ -f /home/user/docs/report.txt ] && [ -f /home/user/docs/report.txt.xz ]; then
  if grep -q 'Annual Report 2023' /home/user/docs/report.txt && grep -q 'Summary: Profits increased.' /home/user/docs/report.txt; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
