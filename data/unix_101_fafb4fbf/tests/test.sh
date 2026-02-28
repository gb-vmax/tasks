#!/bin/bash
expected=$'# User 123 logged in\nError: code 404'
actual=$(egrep '[0-9]' /home/user/app.log)
if [ "$actual" == "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
