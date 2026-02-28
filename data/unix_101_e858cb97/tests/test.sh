#!/bin/bash
if typeset -f greet >/dev/null 2>&1; then
  echo 0 > /logs/verifier/reward.txt
else
  echo 1 > /logs/verifier/reward.txt
fi
