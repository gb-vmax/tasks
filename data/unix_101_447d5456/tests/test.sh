#!/bin/bash
if [ ! -L /home/user/link_to_data.txt ] && [ -f /home/user/data.txt ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
