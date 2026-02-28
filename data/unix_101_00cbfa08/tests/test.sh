#!/bin/bash
expected=$'[ ] B\n] Cal\n[ ] R'
if [[ -f /home/user/notes/todo_cut.txt ]]; then
  diff -q /home/user/notes/todo_cut.txt <(printf "%s" "$expected") && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
