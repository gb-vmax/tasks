#!/bin/bash
expected='Section 3 content---END---\nSection 2 content---END---\nSection 1 content'
actual=$(cat /home/user/reversed_sections.txt | tr -d '\r')
if [ "$actual" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
