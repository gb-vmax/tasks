#!/bin/bash
set -e
cd /home/user

ls /home/user/api_data/
head -5 /home/user/api_data/users.tsv && echo "---" && head -5 /home/user/api_data/scores.tsv && echo "---" && head -5 /home/user/api_data/regions.tsv
mkdir -p /home/user/api_data/output
awk 'BEGIN{FS="\t"; OFS="\t"} {print $2, $4, $3, $6, $5}' /home/user/api_data/users.tsv > /home/user/api_data/output/normalized_users.tsv
paste /home/user/api_data/users.tsv /home/user/api_data/scores.tsv /home/user/api_data/regions.tsv | awk 'BEGIN{FS="\t"; OFS="\t"} {print $2, $4, $3, $9, $8, $12, $13, $5}' > /home/user/api_data/output/combined_report.tsv
echo "=== normalized_users.tsv ===" && cat /home/user/api_data/output/normalized_users.tsv && echo "=== combined_report.tsv ===" && cat /home/user/api_data/output/combined_report.tsv
