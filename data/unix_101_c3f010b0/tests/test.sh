#!/bin/bash
SUCCESS=1
for PID in $(cat /home/user/userpids.txt); do
  if [ ! -d "/proc/$PID" ]; then SUCCESS=0; break; fi
  CUR_NICE=$(ps -o ni= -p $PID | awk '{print $1}')
  if [ "$CUR_NICE" != "10" ]; then SUCCESS=0; break; fi
done
echo $SUCCESS > /logs/verifier/reward.txt
