#!/bin/bash
PID=$(cat /home/user/echo.pid)
if ps -p "$PID" > /dev/null 2>&1; then
  echo 0 > /logs/verifier/reward.txt
else
  echo 1 > /logs/verifier/reward.txt
fi
