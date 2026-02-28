#!/bin/bash
if [ -f /home/user/unpacked.txt ]; then
  if grep -q 'Compression and decompression with zstd.' /home/user/unpacked.txt; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
