#!/bin/bash
set -e
inode1=$(stat -c %i /home/user/photos/img1.jpg)
inode2=$(stat -c %i /home/user/photos/img2.jpg)
inode3=$(stat -c %i /home/user/photos/img3.jpg)
if [[ "$inode1" == "$inode2" && "$inode1" != "$inode3" ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
