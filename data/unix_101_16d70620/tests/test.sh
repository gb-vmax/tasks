#!/bin/bash
success=1
for f in /home/user/texts/file1.txt /home/user/texts/file2.txt /home/user/texts/file3.txt; do
  if [[ ! -f "$f" ]] || ! grep -qx 'bar' "$f"; then
    success=0
    break
  fi
done
echo $success > /logs/verifier/reward.txt
