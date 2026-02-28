#!/bin/bash
set -e
output="$(cal -A 2 -d 2023-08-15 | sed 's/[[:space:]]*$//')"
expected="    August 2023           September 2023          October 2023\nSu Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa  Su Mo Tu We Th Fr Sa\n       1  2  3  4  5                   1  2  3                   1  2  3  4  5  6  7\n 6  7  8  9 10 11 12   4  5  6  7  8  9 10   8  9 10 11 12 13 14\n13 14 15 16 17 18 19  11 12 13 14 15 16 17  15 16 17 18 19 20 21\n20 21 22 23 24 25 26  18 19 20 21 22 23 24  22 23 24 25 26 27 28\n27 28 29 30 31        25 26 27 28 29 30     29 30 31"
if [ "$output" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
