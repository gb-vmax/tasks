#!/bin/bash
success=1
for f in /home/user/project /home/user/project/main.c /home/user/project/docs /home/user/project/docs/readme.md /home/user/project/.env; do
  owner=$(stat -c '%U' "$f")
  group=$(stat -c '%G' "$f")
  if [ "$owner" != "developer" ] || [ "$group" != "devs" ]; then
    success=0
    break
  fi
done
echo $success > /logs/verifier/reward.txt
