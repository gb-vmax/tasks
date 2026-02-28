#!/bin/bash
owner=$(stat -c '%U' /home/user/report.txt)
group=$(stat -c '%G' /home/user/report.txt)
if [ "$owner" = "root" ] && [ "$group" = "staff" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
