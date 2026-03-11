#!/bin/bash
set -e
cd /home/user

head -20 /home/user/automation/workflow_runs.log
sort /home/user/automation/workflow_runs.log | uniq -c | sort -k1,1rn -k2,2 | awk '{print $1 " " $2}' > /home/user/automation/workflow_frequency.txt
cat /home/user/automation/workflow_frequency.txt
