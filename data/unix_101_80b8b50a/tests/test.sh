#!/bin/bash
if [ ! -f /home/user/data.txt.bz2 ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if [ -f /home/user/data.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
file /home/user/data.txt.bz2 | grep -q 'bzip2 compressed data' && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
