#!/bin/bash
if [ -f /home/user/backup_note.txt ] && cmp -s /home/user/note.txt /home/user/backup_note.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
