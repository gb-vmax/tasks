#!/bin/bash
if last -f /home/user/logs/mywtmp | grep -q "wtmp begins"; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
