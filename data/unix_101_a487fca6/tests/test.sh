#!/bin/bash
out=$(logname --help 2>&1)
if echo "$out" | grep -q "Print the name of the current user." && echo "$out" | grep -q "--help"; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
