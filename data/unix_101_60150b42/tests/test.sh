#!/bin/bash
output=$(sha256sum -c /home/user/data.sha256 2>&1)
if echo "$output" | grep -q '^/home/user/data.bin: OK$'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
