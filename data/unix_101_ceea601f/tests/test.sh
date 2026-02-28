#!/bin/bash
set -e
expected="$(id -Gn user)"
output="$(id -Gn)"
if [ "$output" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
