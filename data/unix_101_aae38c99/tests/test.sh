#!/bin/bash
set -e
cd /home/user
if [ ! -d dir2 ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if [ ! -f dir2/fileB.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if [ "$(cat dir2/fileB.txt)" != "banana" ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# Ensure dir1 and dir3 are not restored
if [ -e dir1 ] || [ -e dir3 ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
echo 1 > /logs/verifier/reward.txt
