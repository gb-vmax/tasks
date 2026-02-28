#!/bin/bash
sleep 1
pgrep -f /home/user/testsleep.sh > /dev/null && echo 0 > /logs/verifier/reward.txt || echo 1 > /logs/verifier/reward.txt
