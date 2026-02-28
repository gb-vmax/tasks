#!/bin/bash
ps -ef | grep '[i]gnore_term.sh' > /dev/null
if [ $? -eq 0 ]; then
  echo 0 > /logs/verifier/reward.txt
else
  echo 1 > /logs/verifier/reward.txt
fi
