#!/bin/bash

set -e
cd /home/user
# Expect three files: xaa, xab, xac
[ -f xaa ] && [ -f xab ] && [ -f xac ] || { echo 0 > /logs/verifier/reward.txt; exit 0; }
# xaa: lines 1-3
head -3 poem.txt | diff - xaa || { echo 0 > /logs/verifier/reward.txt; exit 0; }
# xab: lines 4-6
sed -n '4,6p' poem.txt | diff - xab || { echo 0 > /logs/verifier/reward.txt; exit 0; }
# xac: lines 7-8
sed -n '7,8p' poem.txt | diff - xac || { echo 0 > /logs/verifier/reward.txt; exit 0; }
echo 1 > /logs/verifier/reward.txt
