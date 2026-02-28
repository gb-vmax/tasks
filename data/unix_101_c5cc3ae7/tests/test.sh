#!/bin/bash
# Test that errno -l produced a non-empty list including at least a few well-known codes
if [ -s /home/user/errno_all.txt ] && grep -q "ENOENT" /home/user/errno_all.txt && grep -q "EACCES" /home/user/errno_all.txt && grep -qi "No such file or directory" /home/user/errno_all.txt && grep -qi "Permission denied" /home/user/errno_all.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
