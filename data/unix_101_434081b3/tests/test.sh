#!/bin/bash
set -e
# Capture output lines (sorted, as find order is not guaranteed)
expected='/home/user/docs/file1.txt
/home/user/docs/subdir1/notes.txt
/home/user/docs/subdir2/readme.txt'
actual=$(find /home/user/docs -name '*.txt' | sort)
if [ "$actual" = "$expected" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
