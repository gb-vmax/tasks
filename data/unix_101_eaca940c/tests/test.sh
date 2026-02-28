#!/bin/bash
sleep 1  # Give time for background lock to persist
if [[ ! -f /home/user/test.txt ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
