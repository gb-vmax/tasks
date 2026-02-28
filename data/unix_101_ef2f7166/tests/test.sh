#!/bin/bash
if [ ! -f /home/user/output.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if [ "$(wc -l < /home/user/output.txt)" -ne 10 ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if grep -vq '^y$' /home/user/output.txt; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
echo 1 > /logs/verifier/reward.txt
