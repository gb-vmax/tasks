#!/bin/bash
if [ ! -f /home/user/result1.txt ]; then echo 0 > /logs/verifier/reward.txt; exit; fi
if grep -qxF 'apple' /home/user/result1.txt && grep -qxF 'banana' /home/user/result1.txt && grep -qxF 'cherry' /home/user/result1.txt && [ $(wc -l < /home/user/result1.txt) -eq 3 ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
