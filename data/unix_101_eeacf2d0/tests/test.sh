#!/bin/bash
if grep -q 'USER' /home/user/all_processes.txt && grep -q 'ps aux' /home/user/all_processes.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
