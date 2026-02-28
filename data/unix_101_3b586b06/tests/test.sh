#!/bin/bash
set -e
if [[ -f /home/user/error_count.txt ]] && [[ $(cat /home/user/error_count.txt) == "3" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
