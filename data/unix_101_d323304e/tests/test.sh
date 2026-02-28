#!/bin/bash
if [ ! -f /home/user/formatted1.txt ]; then echo 0 > /logs/verifier/reward.txt; exit; fi
if awk '{ if(length > 40) exit 1 }' /home/user/formatted1.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
