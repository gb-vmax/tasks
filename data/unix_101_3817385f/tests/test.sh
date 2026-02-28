#!/bin/bash
if [ -f /home/user/data.txt.zst ] && [ -f /home/user/data.txt ]; then
  zstd -d -c /home/user/data.txt.zst > /tmp/decompressed.txt
  if cmp -s /tmp/decompressed.txt /home/user/data.txt; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
