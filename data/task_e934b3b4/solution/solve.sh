#!/bin/bash
set -e
cd /home/user

find /home/user/data_analysis -maxdepth 1 -type f -name '*.csv' -printf '%f,%s\n' | sort -t, -k2,2nr > /home/user/data_analysis/csv_disk_usage_report.txt
awk -F, 'BEGIN{count=0;sum=0}{count++;sum+=$2}END{if(count>0){printf "%d\n%d\n%d\n",count,sum,int(sum/count)}else{print "0\n0\n0"}}' /home/user/data_analysis/csv_disk_usage_report.txt > /home/user/data_analysis/csv_disk_usage_summary.txt
cat /home/user/data_analysis/csv_disk_usage_report.txt /home/user/data_analysis/csv_disk_usage_summary.txt
