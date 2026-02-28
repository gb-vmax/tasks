#!/bin/bash
if grep -qi 'text' /home/user/type_output.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
