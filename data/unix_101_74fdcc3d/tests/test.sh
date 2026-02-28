#!/bin/bash
if [ -f /home/user/kernel_name.txt ] && [ $(wc -l < /home/user/kernel_name.txt) -eq 1 ] && [ $(wc -w < /home/user/kernel_name.txt) -eq 1 ] && grep -qE '^[A-Za-z0-9_.-]+$' /home/user/kernel_name.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
