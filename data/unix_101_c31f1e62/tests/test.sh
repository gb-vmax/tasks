#!/bin/bash
set -e
output="$(export -p)"
if echo "$output" | grep -q 'declare -x TESTVAR="foo"' && echo "$output" | grep -q 'declare -x ANOTHERVAR="bar"'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
