#!/bin/bash
if [ ! -f /home/user/data/report.csv.zst ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
if [ -f /home/user/data/report.csv ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Verify decompressed content matches expected
zstd -d -c /home/user/data/report.csv.zst > /tmp/report.csv
if diff -q /tmp/report.csv <(echo -e 'id,name,score\n1,Alice,85\n2,Bob,92'); then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
