#!/bin/bash
if [ ! -f /home/user/logs/tail_bytes.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
size=$(stat -c%s /home/user/logs/tail_bytes.txt)
if [ "$size" -ne 20 ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# Confirm the content matches the last 20 bytes of the original
orig_last20=$(tail -c 20 /home/user/logs/app.log)
out=$(cat /home/user/logs/tail_bytes.txt)
if [ "$orig_last20" = "$out" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
