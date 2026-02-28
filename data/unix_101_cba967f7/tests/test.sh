#!/bin/bash
# Check that changes.txt exists and contains diff3 conflict markers
if [ -f /home/user/changes.txt ] && grep -q '<<<<<<<' /home/user/changes.txt && grep -q '|||||||' /home/user/changes.txt && grep -q '=======' /home/user/changes.txt && grep -q '>>>>>>>' /home/user/changes.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
