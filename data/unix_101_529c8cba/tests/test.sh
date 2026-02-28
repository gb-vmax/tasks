#!/bin/bash
output="$(md5sum -c /home/user/files/MD5SUMS 2>&1)"
echo "$output" | grep -q "/home/user/files/file1.txt: OK" && echo "$output" | grep -q "/home/user/files/file2.txt: OK"
if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
