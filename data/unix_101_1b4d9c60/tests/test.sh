#!/bin/bash
# No direct output or file change can be observed from sync.
# Check that the command is available and ran successfully (non-error exit code assumed).
# For this test, we simply check that the file exists and is readable as before.
if [ -f /home/user/testsync/data.txt ] && grep -q 'A test file for sync' /home/user/testsync/data.txt; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
