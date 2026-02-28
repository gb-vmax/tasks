#!/bin/bash
ref_size=$(stat -c%s /home/user/ref.txt)
input_size=$(stat -c%s /home/user/input.txt)
if [ "$input_size" -eq "$ref_size" ]; then
  # input.txt should be 'short' + 5 zero bytes
  expected=$(printf 'short\x00\x00\x00\x00\x00')
  actual=$(cat /home/user/input.txt)
  if [ "$actual" = "$expected" ]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
