#!/bin/bash
EXPECTED="# This is a comment that
# should be wrapped to the
# specified width.
Normal text that should not be changed.
# Another comment that is also very
# long and should be wrapped
# nicely."
if [[ -f /home/user/data/prefixed_fmt.txt ]] && diff -u <(echo "$EXPECTED") /home/user/data/prefixed_fmt.txt >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
