#!/bin/bash
expected=$'vacation1\nvacation2'
output=$(basename -a -s .jpg /home/user/photos/vacation1.jpg /home/user/photos/vacation2.jpg)
if [ "$output" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
