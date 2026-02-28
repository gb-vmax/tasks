#!/bin/bash
if [[ -f /home/user/ping_result.txt ]] && grep -q '2 packets transmitted' /home/user/ping_result.txt && grep -q '2 received' /home/user/ping_result.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
