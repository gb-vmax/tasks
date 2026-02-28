#!/bin/bash
if [ ! -f /home/user/note.txt.zst ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
if [ ! -f /home/user/note.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Verify decompressed content matches original
zstd -d -c /home/user/note.txt.zst > /tmp/unzstd.txt
if diff -q /tmp/unzstd.txt /home/user/note.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
