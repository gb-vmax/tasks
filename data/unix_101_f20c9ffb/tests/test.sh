#!/bin/bash
if [[ -f "/home/user/notes.txt.gz" && ! -f "/home/user/notes.txt" ]]; then
  gunzip -c /home/user/notes.txt.gz | grep -q 'Meeting notes:' && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
