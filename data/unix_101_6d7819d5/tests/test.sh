#!/bin/bash
expected="2fd4e1c67a2d28fced849ee1bb76e7391b93eb12  /home/user/data.txt"
if [ -f /home/user/data.sha1 ] && grep -Fxq "$expected" /home/user/data.sha1; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
