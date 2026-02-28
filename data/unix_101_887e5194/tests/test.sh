#!/bin/bash
result=$(whereis -m -M /home/user/customman -f customtool)
if [[ "$result" == *"/home/user/customman/man1/customtool.1"* && "$result" != *"/home/user/bin/customtool"* ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
