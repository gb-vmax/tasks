#!/bin/bash
cksum_output=$(cksum /home/user/note.txt)
file_output=$(cat /home/user/note_cksum.txt)
if [ "$cksum_output" = "$file_output" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
