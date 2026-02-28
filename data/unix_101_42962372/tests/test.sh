#!/bin/bash
output=$(stat -c %A /home/user/subdir/script.sh)
if [ "$output" = "-rwxr-xr--" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
