#!/bin/bash
if [ ! -f /home/user/dec2023.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# December 2023 starts on a Friday, has 31 days. Ensure 'December 2023' appears and 31 is present.
grep -q "December 2023" /home/user/dec2023.txt && grep -q "31" /home/user/dec2023.txt && grep -q "Su Mo Tu We Th Fr Sa" /home/user/dec2023.txt && [ $(wc -l < /home/user/dec2023.txt) -ge 6 ] && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
