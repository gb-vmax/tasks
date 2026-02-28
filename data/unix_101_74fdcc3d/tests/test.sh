#!/bin/bash
output=$(uname -s)
agents_output=$(uname -s)
if [ "$output" = "$agents_output" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
