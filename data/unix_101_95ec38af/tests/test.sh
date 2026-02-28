#!/bin/bash
if [ ! -s /home/user/locales.txt ]; then
  echo 0 > /logs/verifier/reward.txt
  exit 0
fi
# Check that at least 'C' and 'POSIX' are present (these are always available)
grep -q '^C$' /home/user/locales.txt && grep -q '^POSIX$' /home/user/locales.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
