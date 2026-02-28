#!/bin/bash
if [ -d /home/user/data/2024/reports ]; then
  perms=$(stat -c '%a' /home/user/data/2024/reports)
  if [ "$perms" = "700" ]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
