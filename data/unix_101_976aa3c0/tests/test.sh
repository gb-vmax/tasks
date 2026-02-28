#!/bin/bash
if df -h | grep -E 'Filesystem|Mounted on'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
