#!/bin/bash
lsattr -R /home/user/data > /tmp/lsattr_recursive.txt 2>/dev/null
if grep -q 'file1.txt' /tmp/lsattr_recursive.txt && grep -q 'file2.txt' /tmp/lsattr_recursive.txt && grep -q 'archive/file3.txt' /tmp/lsattr_recursive.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
