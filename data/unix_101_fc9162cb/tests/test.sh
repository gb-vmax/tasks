#!/bin/bash
output="$(xzcat /home/user/data/hello.txt.xz 2>/dev/null)"
if [ "$output" = "Hello, xzcat!" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
