#!/bin/bash
limit=$(ulimit -Sn)
if [ "$limit" -eq 128 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
