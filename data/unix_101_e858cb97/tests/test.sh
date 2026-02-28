#!/bin/bash
# Try to call the function after it has been unset
if bash -c 'greet' 2>/dev/null; then
  echo 0 > /logs/verifier/reward.txt
else
  echo 1 > /logs/verifier/reward.txt
fi
