#!/bin/bash
if [ -f /home/user/notes.txt ]; then
  if [ ! -s /home/user/notes.txt ]; then
    echo 1 > /logs/verifier/reward.txt
  else
    echo 0 > /logs/verifier/reward.txt
  fi
else
  echo 0 > /logs/verifier/reward.txt
fi
