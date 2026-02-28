#!/bin/bash
set -e
EXPECTED="00000000  48 65 6c 6c 6f 2c 20 55  6e 69 78 21 0a              |Hello, Unix!.|\n0000000d"
OUTPUT=$(cat /home/user/data/hello.hex | tr -d '\r')
# Only compare the first line, as hexdump output may add a trailing line with the offset
if [[ "$OUTPUT" == *"48 65 6c 6c 6f 2c 20 55  6e 69 78 21 0a              |Hello, Unix!.|"* ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
