#!/bin/bash
pass=1
for f in "/home/user/project" "/home/user/project/main.py" "/home/user/project/subdir" "/home/user/project/subdir/test.py"; do
  if [ "$(stat -c %G "$f")" != "managers" ]; then
    pass=0
    break
  fi
done
echo $pass > /logs/verifier/reward.txt
