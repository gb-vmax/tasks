#!/bin/bash
expected='1 Alice London
2 Bob Paris
3 Carol Berlin'
if [[ -f /home/user/people_cities.txt ]] && diff -u <(echo "$expected") /home/user/people_cities.txt >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
