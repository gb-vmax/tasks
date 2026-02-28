#!/bin/bash
if [ -f /home/user/system.log.bz2 ] && [ ! -f /home/user/system.log ]; then
  bunzip2 -t /home/user/system.log.bz2 && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
