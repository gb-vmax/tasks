#!/bin/bash
cksum1=$(cksum /home/user/data/food.txt)
cksum2=$(cksum /home/user/data/animals.txt)
cksum3=$(cksum /home/user/data/colors.txt)
output=$(cat /home/user/data_checksums.txt)
if echo "$output" | grep -q "$cksum1" && echo "$output" | grep -q "$cksum2" && echo "$output" | grep -q "$cksum3" && [ $(wc -l < /home/user/data_checksums.txt) -eq 3 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
