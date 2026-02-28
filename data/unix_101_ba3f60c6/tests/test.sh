#!/bin/bash
EXPECTED=$'\ta\tb\tc\n\t\tindented\n\tmid\tspaces\nno_spaces'
if [[ -f /home/user/code/tabs.txt ]] && diff -u <(printf "%s" "$EXPECTED") /home/user/code/tabs.txt >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
