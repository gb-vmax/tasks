#!/bin/bash
set -e
found=0
for f in /home/user/mytempfile_*; do
  if [[ "$f" =~ ^/home/user/mytempfile_[A-Za-z0-9]{6}$ ]] && [ -f "$f" ]; then
    found=1
    break
  fi
done
if [ $found -eq 1 ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
