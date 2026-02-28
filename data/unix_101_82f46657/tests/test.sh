#!/bin/bash
expected=$(uname -a)
if [ -f /home/user/sysinfo.txt ] && [ "$(cat /home/user/sysinfo.txt)" = "$expected" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
