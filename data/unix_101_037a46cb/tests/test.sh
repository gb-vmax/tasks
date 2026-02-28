#!/bin/bash
if [[ -f /home/user/vt100_lines.txt ]]; then
  val=$(cat /home/user/vt100_lines.txt)
  # vt100 should always report 24 lines
  if [[ "$val" == "24" ]]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
