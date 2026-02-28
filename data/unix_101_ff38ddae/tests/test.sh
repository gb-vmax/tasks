#!/bin/bash
all_ok=1
for f in "/home/user/data" "/home/user/data/datafile.txt" "/home/user/data/reports" "/home/user/data/reports/report1.txt" "/home/user/data/reports/report2.txt"; do
  owner=$(stat -c %U "$f")
  group=$(stat -c %G "$f")
  if [ "$owner" != "user" ] || [ "$group" != "user" ]; then
    all_ok=0
    break
  fi
done
echo $all_ok > /logs/verifier/reward.txt
