#!/bin/bash
set -e
cd /home/user
if [ ! -f archive.tar ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
rm -f restore1.txt restore2.txt
# Extract to temp files
tar -xf archive.tar file1.txt file2.txt
if ! cmp -s file1.txt <(echo 'Hello world'); then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if ! cmp -s file2.txt <(echo 'Goodbye world'); then echo 0 > /logs/verifier/reward.txt; exit 0; fi
rm file1.txt file2.txt
echo 1 > /logs/verifier/reward.txt
