#!/bin/bash
set -e
expected='00000000: 556e 6978 5465 7374                      UnixTest'
if [[ -f /home/user/data/output.hex ]]; then
  # Remove trailing spaces in expected/output for robustness
  file_line=$(head -n1 /home/user/data/output.hex | sed 's/[[:space:]]\+$//')
  exp_line=$(echo "$expected" | sed 's/[[:space:]]\+$//')
  if [[ "$file_line" == "$exp_line" ]]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
