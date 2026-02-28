#!/bin/bash
expected="cdef"
if [ -f /home/user/substr.txt ] && grep -qx "$expected" /home/user/substr.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
