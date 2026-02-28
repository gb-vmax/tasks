#!/bin/bash
if [ -f /home/user/backup.txt ] && [ -f /home/user/document.txt ]; then
  if [ "$(cat /home/user/backup.txt)" = "This is the original file." ]; then
    orig_inode=$(stat -c %i /home/user/document.txt)
    link_inode=$(stat -c %i /home/user/backup.txt)
    if [ "$orig_inode" = "$link_inode" ]; then
      echo 1 > /logs/verifier/reward.txt
      exit 0
    fi
  fi
fi
echo 0 > /logs/verifier/reward.txt
