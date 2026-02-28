#!/bin/bash
if [[ -f /home/user/data.txt && ! -f /home/user/data.txt.bz2 ]]; then
  if cmp -s /home/user/data.txt <(echo 'Example data for bunzip2.'); then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
