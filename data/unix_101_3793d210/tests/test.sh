#!/bin/bash
if [ ! -f /home/user/sample.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
actual_size=$(stat -c%s /home/user/sample.txt)
if [ "$actual_size" -eq 10 ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
