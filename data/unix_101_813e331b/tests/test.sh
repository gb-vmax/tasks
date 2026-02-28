#!/bin/bash
if [ -f /home/user/data/report.txt ] && [ -f /home/user/data/report.txt.bz2 ]; then
  bunzip2 -t /home/user/data/report.txt.bz2 && diff <(cat /home/user/data/report.txt) <(bunzip2 -c /home/user/data/report.txt.bz2) >/dev/null && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
