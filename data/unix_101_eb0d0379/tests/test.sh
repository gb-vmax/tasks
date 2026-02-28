#!/bin/bash
cd /home/user
if [ ! -f backup.tar ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
files=$(tar -tf backup.tar | sort)
if [ "$files" = "file1.txt
file2.txt" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
