#!/bin/bash
if ss -s | grep -q 'TCP:' && ss -s | grep -q 'UDP:'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
