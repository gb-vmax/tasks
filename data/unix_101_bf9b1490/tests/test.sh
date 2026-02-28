#!/bin/bash
cd /home/user
dir=$(pwd)
output=$(/home/user/pwd_output.txt)
pwd > /home/user/pwd_output.txt
output=$(cat /home/user/pwd_output.txt)
if [ "$output" = "/home/user" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
