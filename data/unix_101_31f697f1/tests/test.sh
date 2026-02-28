#!/bin/bash
if [ ! -f /home/user/last_lines.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
count=$(wc -l < /home/user/last_lines.txt)
if [ "$count" -ne 10 ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
first=$(head -n1 /home/user/last_lines.txt)
last=$(tail -n1 /home/user/last_lines.txt)
if [ "$first" = "Line 6" ] && [ "$last" = "Line 15" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
