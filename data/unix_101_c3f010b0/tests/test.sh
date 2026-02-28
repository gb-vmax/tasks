#!/bin/bash
PASS=1
while read PID; do
  CUR_NICE=$(ps -o ni= -p "$PID" | awk '{print $1}')
  if [ "$CUR_NICE" != "5" ]; then
    PASS=0
    break
  fi
done < /home/user/user_proc_pids.txt
echo $PASS > /logs/verifier/reward.txt
