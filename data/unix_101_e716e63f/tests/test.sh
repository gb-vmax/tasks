#!/bin/bash
set -e
if [ ! -f /home/user/output.txt ]; then
  echo 0 > /logs/verifier/reward.txt; exit 0
fi
# Should contain all original lines, but in any order
for word in apple banana carrot date; do
  grep -qx "$word" /home/user/output.txt || { echo 0 > /logs/verifier/reward.txt; exit 0; }
done
# Should have exactly 4 lines
[ "$(wc -l < /home/user/output.txt)" -eq 4 ] && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
