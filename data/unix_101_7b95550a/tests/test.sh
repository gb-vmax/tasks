#!/bin/bash
EXPECTED=$'apple\tred\nbanana\tyellow\ncherry\tpurple'
if [[ -f /home/user/output.txt ]] && diff <(cat /home/user/output.txt) <(echo "$EXPECTED") >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
