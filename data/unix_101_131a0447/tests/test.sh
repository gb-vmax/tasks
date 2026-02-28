#!/bin/bash
# Check that greet_alias.txt exists and contains the correct alias definition
if [ ! -f /home/user/greet_alias.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
grep -q "alias greet='echo Hello, world!'" /home/user/greet_alias.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
