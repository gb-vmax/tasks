#!/bin/bash
if [ "$(cat /home/user/foo_value.txt)" = "bar" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
