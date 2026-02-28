#!/bin/bash
# Check that env_null.txt contains at least both FOO=bar and BAZ=qux, each null-separated
if grep -zq '^FOO=bar$' /home/user/env_null.txt && grep -zq '^BAZ=qux$' /home/user/env_null.txt; then
  # Check that the file contains nulls
  if LC_ALL=C grep -q "\\x00" /home/user/env_null.txt; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
