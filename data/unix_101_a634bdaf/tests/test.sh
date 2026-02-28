#!/bin/bash
sleep 1
if pgrep sleep > /dev/null; then
  echo 0 > /logs/verifier/reward.txt
else
  echo 1 > /logs/verifier/reward.txt
fi
