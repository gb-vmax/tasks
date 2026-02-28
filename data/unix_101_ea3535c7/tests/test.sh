#!/bin/bash
if [ -f /home/user/archive/data.csv ] && [ -f /home/user/archive/data.csv.bz2 ] && grep -q 'Alice' /home/user/archive/data.csv; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
