#!/bin/bash
if [ ! -d /home/user/emptydir ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
