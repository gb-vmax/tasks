#!/bin/bash
if [ ! -f /home/user/confirmations.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if [ "$(wc -l < /home/user/confirmations.txt)" -ne 5 ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if grep -vq '^accept this$' /home/user/confirmations.txt; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
echo 1 > /logs/verifier/reward.txt
