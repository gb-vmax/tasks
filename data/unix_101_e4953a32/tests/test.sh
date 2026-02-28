#!/bin/bash
output=$(cat /home/user/data/hello.txt)
if [ "$output" = "Hello, Unix world!" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
