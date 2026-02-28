#!/bin/bash
if [ -f /home/user/dest_dir/file1.txt ] && [ -f /home/user/dest_dir/file2.txt ]; then
  diff /home/user/source_dir/file1.txt /home/user/dest_dir/file1.txt && diff /home/user/source_dir/file2.txt /home/user/dest_dir/file2.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
