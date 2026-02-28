#!/bin/bash
pass=1
for f in $(find /home/user/project_dir -print); do
  perm=$(stat -c %a "$f")
  if [ "$perm" != "755" ]; then
    pass=0
    break
  fi
done
echo $pass > /logs/verifier/reward.txt
