#!/bin/bash
expected='Name    Age     City
Alice   23      Paris
Bob     30      London
'
if [[ -f /home/user/data/spaces.txt ]] && diff -u <(printf "$expected") /home/user/data/spaces.txt >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
