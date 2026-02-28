#!/bin/bash
PID=$(cat /home/user/sleeppid.txt)
if [ ! -d "/proc/$PID" ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
CUR_NICE=$(ps -o ni= -p $PID | awk '{print $1}')
if [ "$CUR_NICE" = "5" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
