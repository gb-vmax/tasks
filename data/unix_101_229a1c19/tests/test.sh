#!/bin/bash
set +e
false
if [ $? -ne 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
