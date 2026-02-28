#!/bin/bash
ret=1
if [[ ! -f /home/user/docs/report.txt && ! -f /home/user/docs/summary.txt ]]; then
  if [[ "$(cat /home/user/backup/report.txt)" == "April report" && "$(cat /home/user/backup/report.txt~)" == "Old report" ]]; then
    if [[ "$(cat /home/user/backup/summary.txt)" == "Short summary" && "$(cat /home/user/backup/summary.txt~)" == "Backup summary" ]]; then
      echo 1 > /logs/verifier/reward.txt
      exit 0
    fi
  fi
fi
echo 0 > /logs/verifier/reward.txt
