#!/bin/bash
expected='[
  {
    "id": 1,
    "name": "Alice"
  },
  {
    "id": 2,
    "name": "Bob"
  },
  {
    "id": 3,
    "name": "Charlie"
  }
]'
if [ ! -f /home/user/users.json ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
actual=$(cat /home/user/users.json)
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
