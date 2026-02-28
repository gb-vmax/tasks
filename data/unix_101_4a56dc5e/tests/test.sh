#!/bin/bash
set -e
cd /home/user
if [ ! -f archive.zip ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
unzip -p archive.zip file1.txt > extracted1.txt || { echo 0 > /logs/verifier/reward.txt; exit 0; }
unzip -p archive.zip file2.txt > extracted2.txt || { echo 0 > /logs/verifier/reward.txt; exit 0; }
diff -q file1.txt extracted1.txt && diff -q file2.txt extracted2.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
