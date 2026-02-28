#!/bin/bash
if [[ -f "/home/user/data/report.csv" && -f "/home/user/data/report.csv.gz" ]]; then
  gunzip -c /home/user/data/report.csv.gz | cmp -s /home/user/data/report.csv - && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
