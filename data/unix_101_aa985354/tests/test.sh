#!/bin/bash
if [[ $(cat /home/user/match_count.txt) == "4" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
