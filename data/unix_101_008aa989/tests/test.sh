#!/bin/bash
if [ ! -e /home/user/temp_dir ] && [ ! -e /home/user/temp_dir/file1.txt ] && [ ! -e /home/user/temp_dir/subdir/file2.txt ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
