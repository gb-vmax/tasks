#!/bin/bash
cd /home/user
if [ ! -f output/main.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if [ ! -f output/subdir/sub.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if grep -q 'main file' output/main.txt && grep -q 'sub content' output/subdir/sub.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
