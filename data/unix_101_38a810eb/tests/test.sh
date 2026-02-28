#!/bin/bash
if [ /home/user/project/new.txt -nt /home/user/project/old.txt ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
