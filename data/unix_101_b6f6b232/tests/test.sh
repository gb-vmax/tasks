#!/bin/bash
if [ "$(cat /home/user/greeting.txt | tr -d '\n')" = "hello_world" ]; then
  echo "1" > /logs/verifier/reward.txt
else
  echo "0" > /logs/verifier/reward.txt
fi
