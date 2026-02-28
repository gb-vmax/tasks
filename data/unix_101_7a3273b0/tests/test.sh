#!/bin/bash
if dircolors --print-database | grep -q '^DIR'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
