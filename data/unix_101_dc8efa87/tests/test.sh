#!/bin/bash
pid=$(pgrep -u user -f 'tail -f /home/user/temp/session.lock')
if [ -z "$pid" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  kill "$pid" 2>/dev/null
  echo 0 > /logs/verifier/reward.txt
fi
