#!/bin/bash
EXPECTED=$'\tThis is line one\n\t\tThis is line two\n\tAnother indented line\nNoIndentHere'
if [[ -f /home/user/docs/indented_unexpanded.txt ]] && diff -u <(printf "%s" "$EXPECTED") /home/user/docs/indented_unexpanded.txt >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
