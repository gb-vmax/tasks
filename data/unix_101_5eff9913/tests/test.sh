#!/bin/bash
OUT=$(uptime -p)
if [[ "$OUT" == up* ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
