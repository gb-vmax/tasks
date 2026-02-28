#!/bin/bash
umask_val=$(umask)
if [ "$umask_val" = "0022" ]; then
  # Now check that a new file is not writable by group or others
  cd /home/user/test_umask
  touch file1
  perms=$(stat -c %a file1)
  # With umask 022, default file should be 644
  if [ "$perms" = "644" ]; then
    echo 1 > /logs/verifier/reward.txt
    exit 0
  fi
fi
echo 0 > /logs/verifier/reward.txt
