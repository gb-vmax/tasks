#!/bin/bash
if [ -f /home/user/lc_time_keywords.txt ]; then
  grep -q '^abday=' /home/user/lc_time_keywords.txt && grep -q '^date_fmt=' /home/user/lc_time_keywords.txt && grep -q '^mon=' /home/user/lc_time_keywords.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
