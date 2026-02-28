#!/bin/bash
if [ ! -f /home/user/ignored_proc.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
orig=$(nproc)
val=$(cat /home/user/ignored_proc.txt)
if [ "$orig" -le 1 ]; then
  # nproc --ignore=1 returns at least 1
  if [ "$val" = "1" ]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  else
    echo 0 > /logs/verifier/reward.txt
    exit 0
  fi
fi
expected=$((orig-1))
if [ "$val" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
