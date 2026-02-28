#!/bin/bash
if [ ! -f /home/user/files/sum_bsd.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
expected="$(sum -r /home/user/files/sample.bin)"
actual="$(cat /home/user/files/sum_bsd.txt)"
if [ "$expected" = "$actual" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
