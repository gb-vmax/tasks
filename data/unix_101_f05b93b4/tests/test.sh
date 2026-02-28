#!/bin/bash
if [ ! -f /home/user/interfaces.json ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
if grep -q '"ifname"' /home/user/interfaces.json && grep -q '\[' /home/user/interfaces.json; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
