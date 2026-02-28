#!/bin/bash
out=$(umask)
if [ "$out" = "0027" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
