#!/bin/bash
set +e
procs=$(pgrep -u user sleep | wc -l)
if [ "$procs" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
