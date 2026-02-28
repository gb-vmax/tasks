#!/bin/bash
if [ /home/user/second.txt -nt /home/user/first.txt ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
