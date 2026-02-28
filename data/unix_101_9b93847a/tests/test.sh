#!/bin/bash
set -e
if grep -q '^locked$' /home/user/lockfile.log; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
