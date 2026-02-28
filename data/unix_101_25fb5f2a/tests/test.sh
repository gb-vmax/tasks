#!/bin/bash
source /home/user/env_setup.sh
if [ "$MYVAR" = "hello" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
