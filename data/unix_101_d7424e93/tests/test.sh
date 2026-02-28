#!/bin/bash
set +e
user_procs=$(pgrep -u user -x mywait | wc -l)
root_procs=$(pgrep -u root -x mywait | wc -l)
if [ "$user_procs" -eq 0 ] && [ "$root_procs" -ge 1 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
