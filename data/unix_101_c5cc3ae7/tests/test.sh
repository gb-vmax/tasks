#!/bin/bash
if grep -q -E '^ 2[[:space:]]+ENOENT[[:space:]]+' /home/user/all_errno.txt && grep -q -E '^ 13[[:space:]]+EACCES[[:space:]]+' /home/user/all_errno.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
