#!/bin/bash
expected='[
  {
    "id": 2,
    "value": "B"
  },
  {
    "id": 3,
    "value": "C"
  },
  {
    "id": 1,
    "value": "A"
  }
]'
actual="$(cat /home/user/merged.json 2>/dev/null)"
if [ "$actual" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
