#!/bin/bash
if [ -f /home/user/all_processes.txt ] && grep -q "PID" /home/user/all_processes.txt && grep -q "USER" /home/user/all_processes.txt && [ $(wc -l < /home/user/all_processes.txt) -gt 1 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
