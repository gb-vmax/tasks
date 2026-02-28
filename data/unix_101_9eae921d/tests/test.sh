#!/bin/bash
set -e
EXPECTED=(/home/user/report.txt /home/user/docs/report.txt /home/user/docs/hr/report.txt /home/user/docs/finance/report.txt)
FOUND=($(locate report.txt | grep '^/home/user/'))
pass=1
for e in "${EXPECTED[@]}"; do
  found=0
  for f in "${FOUND[@]}"; do
    if [[ "$f" == "$e" ]]; then
      found=1
      break
    fi
  done
  if [[ $found -eq 0 ]]; then
    pass=0
    break
  fi
done
if [[ $pass -eq 1 && ${#FOUND[@]} -eq ${#EXPECTED[@]} ]]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
