#!/bin/bash
set +e
OUT=$(diff -r -w /home/user/dir1 /home/user/dir2)
if [ -z "$OUT" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
