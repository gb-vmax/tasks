#!/bin/bash
set -e
EXPECTED='apple
banana
carrot'
ACTUAL=$(zcat /home/user/data.txt.gz)
if [ "$ACTUAL" = "$EXPECTED" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
