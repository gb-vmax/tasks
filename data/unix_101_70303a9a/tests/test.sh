#!/bin/bash
set -e
pid=$(cat /home/user/run_pid.txt)
grep -q "$pid" /home/user/pid_lsof.txt && [ -s /home/user/pid_lsof.txt ] && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
