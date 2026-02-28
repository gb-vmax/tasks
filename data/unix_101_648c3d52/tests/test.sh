#!/bin/bash
if [ ! -f /home/user/output.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
grep -q '^Hello World$' /home/user/output.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
