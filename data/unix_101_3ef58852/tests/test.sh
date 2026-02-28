#!/bin/bash
EXPECTED=$'A1;A2;A3\nB1;B2'
if [[ -f /home/user/merged.txt ]] && diff <(cat /home/user/merged.txt) <(echo "$EXPECTED") >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
