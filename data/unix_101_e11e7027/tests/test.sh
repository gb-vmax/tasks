#!/bin/bash
if [[ -f /home/user/term_cols.txt ]]; then
  val=$(cat /home/user/term_cols.txt)
  if [[ "$val" =~ ^[0-9]+$ ]] && (( val > 0 )); then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
