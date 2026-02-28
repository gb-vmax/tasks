#!/bin/bash
if ulimit -a | grep -q "open files" && ulimit -a | grep -q "max user processes"; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
