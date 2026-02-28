#!/bin/bash
if grep -q '{+quickly+}' /home/user/insertions.txt && ! grep -q '{-' /home/user/insertions.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
