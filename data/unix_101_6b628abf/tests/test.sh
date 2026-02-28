#!/bin/bash
if env | grep -q '^TEMP_VAR='; then
  echo 0 > /logs/verifier/reward.txt
else
  echo 1 > /logs/verifier/reward.txt
fi
