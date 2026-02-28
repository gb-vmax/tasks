#!/bin/bash
expected='name
Alice
Bob
Carol'
if [[ -f /home/user/first_column.txt ]] && diff -u <(echo "$expected") /home/user/first_column.txt >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
