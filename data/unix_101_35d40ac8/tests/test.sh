#!/bin/bash
output=$(readlink /home/user/link1)
if [ "$output" = "/home/user/file1.txt" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
