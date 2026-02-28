#!/bin/bash
if [ -e /home/user/old_data.bin ]; then
  echo 0 > /logs/verifier/reward.txt
else
  echo 1 > /logs/verifier/reward.txt
fi
