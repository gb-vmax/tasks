#!/bin/bash
if [[ -f /home/user/data/usernames.txt ]]; then
  diff -q /home/user/data/usernames.txt <(printf "alice\nbob\ncarol\n") && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
