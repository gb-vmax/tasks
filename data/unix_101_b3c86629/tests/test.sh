#!/bin/bash
expected="5 /home/user/doc1.txt"
expected2="5 /home/user/doc2.txt"
total="10 total"
output="$(wc -w /home/user/doc1.txt /home/user/doc2.txt)"
if echo "$output" | grep -q "$expected" && echo "$output" | grep -q "$expected2" && echo "$output" | grep -q "$total"; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
