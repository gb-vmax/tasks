#!/bin/bash
set -e
cd /home/user

awk -F, 'NR>1 {a[$1]+=$3; b[$1]++} END{for(i in a){avg=a[i]/b[i];if(avg>max){max=avg;dept=i}} printf "{\"department\": \"%s\", \"avg_cpu_usage\": %.2f}\n", dept, max}' /home/user/data/resource_usage.csv > /home/user/data/dept_with_highest_avg_cpu.json
cat /home/user/data/dept_with_highest_avg_cpu.json
