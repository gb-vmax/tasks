#!/bin/bash
if [[ ! -f /home/user/rev_help.txt ]]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
grep -q 'Reverse lines characterwise.' /home/user/rev_help.txt && grep -q 'Usage: rev' /home/user/rev_help.txt && grep -q -- '--help' /home/user/rev_help.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
