#!/bin/bash
if [[ $(cat /home/user/apples.txt) == $'apple pie
apple' ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
