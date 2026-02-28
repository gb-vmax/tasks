#!/bin/bash
if [ -p /home/user/pipe1 ] && [ ! -f /home/user/pipe1 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
