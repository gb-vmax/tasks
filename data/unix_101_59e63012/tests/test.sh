#!/bin/bash
if [ ! -f /home/user/w_output.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
grep -q "USER" /home/user/w_output.txt && grep -q "TTY" /home/user/w_output.txt && grep -q "WHAT" /home/user/w_output.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
