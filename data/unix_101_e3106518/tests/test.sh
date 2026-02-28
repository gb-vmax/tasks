#!/bin/bash
if [ ! -f /home/user/remove_me.txt ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
