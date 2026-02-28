#!/bin/bash
# Get all PIDs of bash with 'sleep 60' as user
bashpids=$(ps -u user -o pid,comm,args | awk '$2=="bash" && $3=="-c" && $4=="sleep" && $5=="60" {print $1}')
pass=1
for pid in $bashpids; do
  if ! grep -q "^$pid bash$" /home/user/bashlist.txt; then
    pass=0
  fi
done
if [ "$pass" -eq 1 ] && [ "$(wc -l < /home/user/bashlist.txt)" -ge 2 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
