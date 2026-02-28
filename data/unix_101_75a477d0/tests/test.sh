#!/bin/bash
if [ ! -f /home/user/output.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if grep -q '[a-z]' /home/user/output.txt; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if ! grep -q 'HELLO WORLD' /home/user/output.txt; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
echo 1 > /logs/verifier/reward.txt
