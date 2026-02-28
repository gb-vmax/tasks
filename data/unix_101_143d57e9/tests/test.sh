#!/bin/bash
if [[ -f /home/user/todo.txt && ! -f /home/user/note.txt && "$(cat /home/user/todo.txt)" == "Buy groceries" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
