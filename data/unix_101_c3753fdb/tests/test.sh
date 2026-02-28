#!/bin/bash
if [ -f /home/user/partial.bin ] && [ $(stat -c%s /home/user/partial.bin) -eq 12 ]; then
  cmp -n 12 /home/user/large.txt /home/user/partial.bin && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
