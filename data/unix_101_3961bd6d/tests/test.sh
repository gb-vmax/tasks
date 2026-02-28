#!/bin/bash
OWNER=$(stat -c %U /home/user/project.txt)
if [ "$OWNER" = "user" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
