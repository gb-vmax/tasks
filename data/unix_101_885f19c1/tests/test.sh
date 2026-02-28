#!/bin/bash
if set | grep -q '^TEST_VAR=demo_value$'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
