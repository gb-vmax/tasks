#!/bin/bash
if [ ! -f /home/user/ifaces.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
if grep -Eq '^lo\s+UNKNOWN' /home/user/ifaces.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
