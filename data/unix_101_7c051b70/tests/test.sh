#!/bin/bash
if [ ! -f /home/user/meminfo.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
if grep -q 'total' /home/user/meminfo.txt && grep -q 'free' /home/user/meminfo.txt; then
  if grep -E -q '[0-9]+[GgMmKk]' /home/user/meminfo.txt; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
