#!/bin/bash
out=$(zgrep -i 'success' /home/user/data/backup1.gz /home/user/data/backup2.gz)
expected='/home/user/data/backup1.gz:Success! Backup completed.
/home/user/data/backup2.gz:Partial success on backup.'
if [[ "$out" == "$expected" ]]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
