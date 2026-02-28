#!/bin/bash
output=$(zcat /home/user/app.log.gz)
if [ "$output" = $'Log entry 1\nLog entry 2\nLog entry 3' ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
