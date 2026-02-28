#!/bin/bash
if [ ! -f /home/user/file2.bin ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
size1=$(stat -c%s /home/user/file1.bin)
size2=$(stat -c%s /home/user/file2.bin)
if [ "$size1" -eq "$size2" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
