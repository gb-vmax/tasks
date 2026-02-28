#!/bin/bash
if [ ! -f /home/user/secret.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
if grep -q 'Top secret information' /home/user/secret.txt; then
  echo 0 > /logs/verifier/reward.txt
else
  echo 1 > /logs/verifier/reward.txt
fi
