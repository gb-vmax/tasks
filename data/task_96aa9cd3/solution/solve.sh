#!/bin/bash
set -e
cd /home/user

cat /home/user/oncall/incidents.log
awk -F'|' '$3 == "CRITICAL" || $3 == "HIGH" {print "[" $3 "] " $2 " | " $4 ": " $5}' /home/user/oncall/incidents.log | sed -e 's/failure/FAILURE/gi' -e 's/timeout/TIMEOUT/gi' > /home/user/oncall/triage_summary.txt
cat /home/user/oncall/triage_summary.txt
