#!/bin/bash
if [ ! -f /home/user/formatted_prefix.txt ]; then echo 0 > /logs/verifier/reward.txt; exit; fi
# Check that all lines starting with '> ' are <= 30 chars
if grep '^> ' /home/user/formatted_prefix.txt | awk '{ if(length > 30) exit 1 }'; then
  # Check that the unprefixed line is present and unmodified
  if grep -qx 'Normal line that should be left untouched.' /home/user/formatted_prefix.txt; then
    echo 1 > /logs/verifier/reward.txt
  else
    echo 0 > /logs/verifier/reward.txt
  fi
else
  echo 0 > /logs/verifier/reward.txt
fi
