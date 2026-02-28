#!/bin/bash
if [[ -f /home/user/quoted.txt ]] && grep -q '^hello\ world!$' /home/user/quoted.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
