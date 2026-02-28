#!/bin/bash
set -e
# Run who on both utmp files and compare output
expected="$(who)"
actual="$(who /home/user/test_utmp)"
if [ "$expected" = "$actual" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
