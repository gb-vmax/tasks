#!/bin/bash
cd /home/user
if [[ -f subdir/fileB.txt && ! -f fileA.txt && ! -f fileC.txt ]]; then
  grep -qx 'Bravo' subdir/fileB.txt && echo 1 > /logs/verifier/reward.txt && exit 0
fi
echo 0 > /logs/verifier/reward.txt
