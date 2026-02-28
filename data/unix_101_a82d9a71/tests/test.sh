#!/bin/bash
if [ ! -f /home/user/data.sum ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Check that the output file has exactly one line and two columns (checksum and blocks)
line_count=$(wc -l < /home/user/data.sum)
col_count=$(awk '{print NF}' /home/user/data.sum)
if [ "$line_count" -eq 1 ] && [ "$col_count" -eq 2 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
