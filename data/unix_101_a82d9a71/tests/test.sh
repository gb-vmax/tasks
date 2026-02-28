#!/bin/bash
if [ ! -f /home/user/sum_output.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
expected="$(sum /home/user/data.txt)"
actual="$(cat /home/user/sum_output.txt)"
if [ "$expected" = "$actual" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
