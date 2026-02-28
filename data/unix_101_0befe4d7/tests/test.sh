#!/bin/bash
if [ ! -f /home/user/error_lines.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
count=$(grep -c '^ERROR' /home/user/error_lines.txt)
if [ "$count" -eq 2 ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
