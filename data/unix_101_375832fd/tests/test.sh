#!/bin/bash
if [ ! -f /home/user/data/scores_expanded.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
if grep -q $'\t' /home/user/data/scores_expanded.txt; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Check that 'ID' is at the start, 'Name' starts at column 5, and 'Score' starts at column 11
line=$(head -n1 /home/user/data/scores_expanded.txt)
col_name=$(echo "$line" | cut -c5-8)
col_score=$(echo "$line" | cut -c11-15)
if [[ "$col_name" != "Name"* ]]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
if [[ "$col_score" != "Score"* ]]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
echo 1 > /logs/verifier/reward.txt
