#!/bin/bash
fail=0
if [ -f /home/user/project_backup/main.py ] && [ -f /home/user/project_backup/README.md ]; then
  if [ -f /home/user/project_backup/build.log ] || [ -f /home/user/project_backup/run.log ]; then
    fail=1
  fi
else
  fail=1
fi
if [ $fail -eq 0 ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
