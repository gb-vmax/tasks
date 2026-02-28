#!/bin/bash
set -e
expected='An apple
Under the sun
Elephant parade
orange juice
Iguana island
umbrella
Egg salad'
output=$(cat /home/user/vowel_lines.txt)
if [ "$output" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
