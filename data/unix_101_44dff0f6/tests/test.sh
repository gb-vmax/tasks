#!/bin/bash
if [ ! -s /home/user/lc_time_keywords.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Check that a well-known LC_TIME keyword is present
grep -q '^abday=' /home/user/lc_time_keywords.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
