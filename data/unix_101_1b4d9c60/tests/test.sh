#!/bin/bash
# There is no direct way to verify sync except that the command completes successfully
# We'll check that the files still exist and have the correct contents
if [[ $(cat /home/user/testdir/file1.txt) == 'data1' && $(cat /home/user/testdir/file2.txt) == 'data2' ]]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
