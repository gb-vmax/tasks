#!/bin/bash
cd /home/user/link_folder
output=$(pwd -P)
if [ "$output" = "/home/user/real_folder" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
