#!/bin/bash
set -e
# Should exit 0 and produce no output
if pathchk /home/user/notes/todo.txt 2>/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
