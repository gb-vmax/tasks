#!/bin/bash
if [ ! -f /home/user/jan2020_julian.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# The Julian calendar for Jan 2020 starts with 1 and ends with 31
# The first week should contain numbers 1 to 4
head -n 3 /home/user/jan2020_julian.txt | grep -Eq '^[[:space:]]*1[[:space:]]+2[[:space:]]+3[[:space:]]+4'
if [ $? -ne 0 ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Last line should contain 31
if ! grep -q '\b31\b' /home/user/jan2020_julian.txt; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Check for 'January 2020' in the header
head -n 1 /home/user/jan2020_julian.txt | grep -q 'January 2020'
if [ $? -ne 0 ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
echo 1 > /logs/verifier/reward.txt
