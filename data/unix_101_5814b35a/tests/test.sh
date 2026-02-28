#!/bin/bash
set -e
out=$(nice)
if [[ $out =~ ^[0-9]+$ ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
