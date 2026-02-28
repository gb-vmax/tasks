#!/bin/bash
EXPECTED='     1	First line

     2	Second line


     3	Third line'
ACTUAL=$(cat /home/user/numbered.txt)
if [ "$ACTUAL" == "$EXPECTED" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
