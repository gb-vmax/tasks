#!/bin/bash
user_uid=$(id -u user)
# Get PID of tail process
pid=$(pgrep -u user -x tail | head -n1)
lsof_output=$(lsof -u user -l)
if [ -z "$pid" ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
# Check that the output contains the PID and the UID number
if echo "$lsof_output" | grep -q "$pid" && echo "$lsof_output" | grep -qw "$user_uid"; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
