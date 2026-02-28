#!/bin/bash
# After skipping 5 bytes, both files have '12345FGHIJ' (alpha) and 'XXXXXFGHIJ' (beta), so they differ.
if cmp --ignore-initial=5 -s /home/user/alpha.bin /home/user/beta.bin; then
  echo 0 > /logs/verifier/reward.txt
else
  echo 1 > /logs/verifier/reward.txt
fi
