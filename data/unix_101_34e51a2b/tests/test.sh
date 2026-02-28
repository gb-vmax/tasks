#!/bin/bash
expected='     1	Buy milk
     2	Walk the dog
     3	Call mom'
output=$(cat -n /home/user/notes/todo.txt)
if [ "$output" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
