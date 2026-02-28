#!/bin/bash
set -e
if ulimit -a > /tmp/ulimit_actual.txt; then
  if diff /tmp/ulimit_actual.txt <(ulimit -a) >/dev/null; then
    echo 1 > /logs/verifier/reward.txt
  else
    echo 0 > /logs/verifier/reward.txt
  fi
else
  echo 0 > /logs/verifier/reward.txt
fi
