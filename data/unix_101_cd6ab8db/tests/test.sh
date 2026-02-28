#!/bin/bash
if [ ! -f /home/user/a2.o ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
if [ -f /home/user/a1.o ] || [ -f /home/user/a3.o ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
if cmp -s /home/user/a2.o <(echo 'bbb'); then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
