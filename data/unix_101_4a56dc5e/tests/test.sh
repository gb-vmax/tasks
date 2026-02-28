#!/bin/bash
set -e
cd /home/user
# Check the zip file exists
[ -f archive.zip ] || { echo 0 > /logs/verifier/reward.txt; exit; }
# Check both files are present in the zip
unzip -l archive.zip | grep -q 'file1.txt' || { echo 0 > /logs/verifier/reward.txt; exit; }
unzip -l archive.zip | grep -q 'file2.txt' || { echo 0 > /logs/verifier/reward.txt; exit; }
echo 1 > /logs/verifier/reward.txt
