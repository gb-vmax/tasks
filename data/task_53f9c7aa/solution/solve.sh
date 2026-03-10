#!/bin/bash
set -e
cd /home/user

cat /home/user/mlops/artifact_log.txt
sort /home/user/mlops/artifact_log.txt | uniq -c | sort -k1,1rn -k2,2 | awk '{print $1, $2}' > /home/user/mlops/artifact_counts.txt
cat /home/user/mlops/artifact_counts.txt
