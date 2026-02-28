#!/bin/bash
if [ -f /home/user/backup/source_data.txt ] && diff /home/user/source_data.txt /home/user/backup/source_data.txt >/dev/null; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
