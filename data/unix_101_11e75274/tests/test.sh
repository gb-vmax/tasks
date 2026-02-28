#!/bin/bash
output=$( { /usr/bin/time -p bash /home/user/test_scripts/hello.sh; } 2>&1 )
if [[ "$output" == *"Hello, world!"* ]] && [[ "$output" == *"real"* ]] && [[ "$output" == *"user"* ]] && [[ "$output" == *"sys"* ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
