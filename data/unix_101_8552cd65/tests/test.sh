#!/bin/bash
output=$(bzcat /home/user/data/hello.txt.bz2 2>/dev/null)
if [[ "$output" == "Hello, bzip2 world!" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
