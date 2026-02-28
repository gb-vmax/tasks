#!/bin/bash
expected=$'Lorem ipsum
dolor sit amet,
consectetur
adipiscing elit.'
if [[ "$(cat /home/user/data/wrapped.txt)" == "$expected" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
