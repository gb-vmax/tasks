#!/bin/bash
# Check merged.txt exists and has diff3 conflict markers (=======, <<<<<<<, >>>>>>>)
if [ -f /home/user/merged.txt ] && grep -q '<<<<<<<' /home/user/merged.txt && grep -q '=======' /home/user/merged.txt && grep -q '>>>>>>>' /home/user/merged.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
