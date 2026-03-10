#!/bin/bash
set -e
cd /home/user

cat /home/user/disk_report.txt
awk 'NR>1 { pct=$5; gsub(/%/,"",pct); if (pct+0 >= 80) printf "ALERT: %s is at %s capacity (%s used of %s)\n", $6, $5, $3, $2 }' /home/user/disk_report.txt > /home/user/alerts.txt
cat /home/user/alerts.txt
