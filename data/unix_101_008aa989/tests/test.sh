#!/bin/bash
if [ ! -e /home/user/project_backup ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
