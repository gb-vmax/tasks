#!/bin/bash
set -e
cd /home/user

python3 /home/user/old_project/main.py > /home/user/old_project/run.log 2>&1
[ -f /home/user/old_project/run.log ] && echo -n "run.log exists: YES" > /home/user/old_project/output_summary.txt && echo -n $'\nOutput preview: ' >> /home/user/old_project/output_summary.txt && head -n 1 /home/user/old_project/run.log >> /home/user/old_project/output_summary.txt
cat /home/user/old_project/output_summary.txt
