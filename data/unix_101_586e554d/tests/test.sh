#!/bin/bash
set -e
# b2sum -c outputs 'OK' on success; we check that the output file exists and is valid
file=/home/user/docs/report.txt
checksum_file=/home/user/docs/report.txt.b2sum
# Tamper check: ensure file still matches checksum
if b2sum -c "$checksum_file" 2>/dev/null | grep -q ': OK'; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
