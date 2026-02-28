#!/bin/bash
if [ -f /home/user/docs/notes.md ] && [ -f /home/user/docs/todo.md ] && [ -f /home/user/docs/readme.md ] && [ ! -f /home/user/docs/notes.txt ] && [ ! -f /home/user/docs/todo.txt ] && [ ! -f /home/user/docs/readme.txt ] && [ -f /home/user/docs/manual.md ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
