#!/bin/bash
sleep 1
if [ -f /home/user/nohup.out ] && grep -q '^Task1 done$' /home/user/nohup.out; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
