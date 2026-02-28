#!/bin/bash
if [ ! -f /home/user/checksums.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# There should be two lines, each with three columns (checksum, blocks, filename)
lines=$(wc -l < /home/user/checksums.txt)
cols1=$(awk 'NR==1{print NF}' /home/user/checksums.txt)
cols2=$(awk 'NR==2{print NF}' /home/user/checksums.txt)
file1=$(awk 'NR==1{print $3}' /home/user/checksums.txt)
file2=$(awk 'NR==2{print $3}' /home/user/checksums.txt)
if [ "$lines" -eq 2 ] && [ "$cols1" -eq 3 ] && [ "$cols2" -eq 3 ] && [[ "$file1" == "/home/user/alpha.txt" ]] && [[ "$file2" == "/home/user/beta.txt" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
