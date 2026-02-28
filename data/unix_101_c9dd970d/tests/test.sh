#!/bin/bash
if [ -f /home/user/data.txt ] && [ ! -f /home/user/data.txt.gz ] && grep -q "Line two" /home/user/data.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
