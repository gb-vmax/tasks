#!/bin/bash
if [ ! -f /home/user/slowcopy.bin ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
if cmp -s /home/user/largefile.bin /home/user/slowcopy.bin; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
