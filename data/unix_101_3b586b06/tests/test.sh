#!/bin/bash
if [ ! -f /home/user/network_count.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
count=$(cat /home/user/network_count.txt | tr -d '[:space:]')
if [ "$count" = "5" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
