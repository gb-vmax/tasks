#!/bin/bash
if pathchk /home/user/my_valid_file.txt > /home/user/pathchk_output.txt 2>&1; then
  if [ ! -s /home/user/pathchk_output.txt ]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
