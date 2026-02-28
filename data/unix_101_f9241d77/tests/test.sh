#!/bin/bash
set -e
inode1=$(stat -c %i /home/user/documents/a/report.txt)
inode2=$(stat -c %i /home/user/documents/b/report.txt)
inode3=$(stat -c %i /home/user/documents/a/summary.txt)
inode4=$(stat -c %i /home/user/documents/b/summary2.txt)
if [[ "$inode1" == "$inode2" && "$inode3" != "$inode4" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
