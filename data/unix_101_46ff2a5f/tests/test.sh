#!/bin/bash
ref_mtime=$(stat -c %Y /home/user/project/template.txt)
target_mtime=$(stat -c %Y /home/user/project/notes.txt)
ref_atime=$(stat -c %X /home/user/project/template.txt)
target_atime=$(stat -c %X /home/user/project/notes.txt)
if [ "$ref_mtime" = "$target_mtime" ] && [ "$ref_atime" = "$target_atime" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
