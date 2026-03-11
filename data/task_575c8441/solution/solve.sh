#!/bin/bash
set -e
cd /home/user

cat /home/user/audit/access_log.tsv
awk -F'\t' 'BEGIN{OFS="\t"} {print $2, $4, $5, $1}' /home/user/audit/access_log.tsv > /home/user/audit/compliance_report.tsv
awk -F'\t' 'NR>1 {print $2}' /home/user/audit/access_log.tsv | sort -u > /home/user/audit/usernames.txt
echo "=== compliance_report.tsv ===" && cat /home/user/audit/compliance_report.tsv && echo "" && echo "=== usernames.txt ===" && cat /home/user/audit/usernames.txt
