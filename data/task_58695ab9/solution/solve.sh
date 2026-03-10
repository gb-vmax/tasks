#!/bin/bash
set -e
cd /home/user

cat /home/user/pipeline/build_failures.log
sort /home/user/pipeline/build_failures.log | uniq -c | sort -k1,1rn -k2 | sed 's/^ *//' > /home/user/pipeline/failure_report.txt
cat /home/user/pipeline/failure_report.txt
