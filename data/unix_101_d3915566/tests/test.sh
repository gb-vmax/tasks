#!/bin/bash
set -e
if [ ! -f /home/user/canon.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
resolved=$(cat /home/user/canon.txt | tr -d '\n')
if [ "$resolved" = "/home/user/realfile.txt" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
