#!/bin/bash
if [ ! -f /home/user/alpha_vs_beta.diff ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# Check that the diff file contains the line with 'date' and the line with 'elderberry'
grep -q '^< date' /home/user/alpha_vs_beta.diff && grep -q '^> elderberry' /home/user/alpha_vs_beta.diff && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
