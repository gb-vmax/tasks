#!/bin/bash
if [[ -f /home/user/archive && -f /home/user/archive.bz2 ]]; then
  if cmp -s /home/user/archive <(echo 'Archive content for bunzip2 test.'); then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
