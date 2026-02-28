#!/bin/bash
sleep_pid=$(pgrep -u user -x sleep | head -n1)
if [ -z "$sleep_pid" ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
lsof_output=$(lsof -c sleep)
if echo "$lsof_output" | grep -q "$sleep_pid"; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
