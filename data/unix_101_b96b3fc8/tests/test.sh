#!/bin/bash
if [ "$1" = "apple" ] && [ "$2" = "banana" ] && [ "$3" = "cherry" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
