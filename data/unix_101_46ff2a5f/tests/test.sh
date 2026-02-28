#!/bin/bash
ref_atime=$(stat -c %X /home/user/reference.txt)
ref_mtime=$(stat -c %Y /home/user/reference.txt)
file_atime=$(stat -c %X /home/user/file.txt)
file_mtime=$(stat -c %Y /home/user/file.txt)
if [ "$ref_atime" = "$file_atime" ] && [ "$ref_mtime" = "$file_mtime" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
