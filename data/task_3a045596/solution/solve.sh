#!/bin/bash
set -e
cd /home/user

head -20 /home/user/artifacts/build_log.txt
sort /home/user/artifacts/build_log.txt | uniq -c | sort -k1,1rn -k2,2 | awk '{print $1, $2}' > /home/user/artifacts/artifact_freq.txt
cat /home/user/artifacts/artifact_freq.txt
total=$(wc -l < /home/user/artifacts/build_log.txt)
unique=$(wc -l < /home/user/artifacts/artifact_freq.txt)
top_line=$(head -1 /home/user/artifacts/artifact_freq.txt)
top_count=$(echo $top_line | awk '{print $1}')
top_name=$(echo $top_line | awk '{print $2}')
echo "Total builds: $total | Unique artifacts: $unique | Most built: $top_name ($top_count times)" > /home/user/artifacts/summary.txt
cat /home/user/artifacts/summary.txt
echo "=== artifact_freq.txt ===" && cat /home/user/artifacts/artifact_freq.txt && echo "=== summary.txt ===" && cat /home/user/artifacts/summary.txt
