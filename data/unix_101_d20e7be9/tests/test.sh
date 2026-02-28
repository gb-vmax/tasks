#!/bin/bash
if [ ! -f /home/user/destination.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if ! grep -q "This is the source file." /home/user/destination.txt; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
perm=$(stat -c %a /home/user/destination.txt)
if [ "$perm" != "600" ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
echo 1 > /logs/verifier/reward.txt
