#!/bin/bash
if [ -p /home/user/fifos/secretpipe ]; then
  perms=$(stat -c '%a' /home/user/fifos/secretpipe)
  if [ "$perms" = "600" ]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
