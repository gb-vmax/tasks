#!/bin/bash
set -e
# Check that all empty files are gone
files=(/home/user/project/file1.txt /home/user/project/alpha/empty1.log /home/user/project/beta/empty2.md /home/user/project/beta/gamma/empty3.tmp)
pass=1
for f in "${files[@]}"; do
  if [ -f "$f" ]; then
    pass=0
  fi
done
# Check that non-empty files still exist
for f in /home/user/project/file2.txt /home/user/project/alpha/data2.csv /home/user/project/beta/gamma/data3.txt; do
  if [ ! -f "$f" ]; then
    pass=0
  fi
done
echo $pass > /logs/verifier/reward.txt
