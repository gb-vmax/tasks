#!/bin/bash
if [ -f /home/user/ls_path.txt ] && [ "$(head -c 1 /home/user/ls_path.txt)" = "/" ] && grep -q "/ls" /home/user/ls_path.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
