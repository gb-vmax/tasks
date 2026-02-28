#!/bin/bash
sleep_running=$(pgrep -u user sleep | wc -l)
if [ "$sleep_running" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
