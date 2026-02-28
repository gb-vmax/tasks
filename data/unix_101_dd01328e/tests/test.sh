#!/bin/bash
if [ ! -f /home/user/all_backups.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# Should match all lines (case-insensitive) with 'backup' from both files.
lines=$(grep -i 'backup' /home/user/all_backups.txt | wc -l)
if [ "$lines" -eq 4 ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
