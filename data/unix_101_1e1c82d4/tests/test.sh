#!/bin/bash
expected="$(md5sum /home/user/data.txt)"
actual="$(cat /home/user/data.md5)"
if [ "$expected" = "$actual" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
