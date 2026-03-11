#!/bin/bash
set -e
cd /home/user

cat /home/user/devsecops/pod_configs.csv
{ echo "POLICY VIOLATION REPORT: privileged=true"; echo "========================================="; awk -F',' 'NR>1 && $4=="true" {print $2"/"$1}' /home/user/devsecops/pod_configs.csv | sort; } > /home/user/devsecops/violations.txt
cat /home/user/devsecops/violations.txt
