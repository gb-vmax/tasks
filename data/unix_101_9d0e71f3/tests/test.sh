#!/bin/bash
EXPECTED="$(cksum /home/user/dir/file1.log)
$(cksum /home/user/dir/file2.log)"
ACTUAL="$(cat /home/user/dir/checksums.txt)"
if [ "$EXPECTED" = "$ACTUAL" ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
