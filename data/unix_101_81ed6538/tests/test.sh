#!/bin/bash
output="$(ss -ltun)"
if echo "$output" | grep -q 'LISTEN' && echo "$output" | grep -qE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
