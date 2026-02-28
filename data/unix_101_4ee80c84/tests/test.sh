#!/bin/bash
set -e
cd /home/user
[ -f project.zip ] || { echo 0 > /logs/verifier/reward.txt; exit; }
# main.py and config.yaml must be present
unzip -l project.zip | grep -q 'project/src/main.py' || { echo 0 > /logs/verifier/reward.txt; exit; }
unzip -l project.zip | grep -q 'project/config.yaml' || { echo 0 > /logs/verifier/reward.txt; exit; }
# tmp/temp1.txt and tmp/cache.dat must NOT be present
! unzip -l project.zip | grep -q 'project/tmp/temp1.txt' || { echo 0 > /logs/verifier/reward.txt; exit; }
! unzip -l project.zip | grep -q 'project/tmp/cache.dat' || { echo 0 > /logs/verifier/reward.txt; exit; }
echo 1 > /logs/verifier/reward.txt
