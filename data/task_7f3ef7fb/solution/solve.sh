#!/bin/bash
set -e
cd /home/user

awk 'NR==FNR {vers[$1]=$2; next} !seen[$1]++ { print $1 "," ( ( $1 in vers ) ? vers[$1] : "UNKNOWN" ) }' /home/user/app-deployment/version-info.txt /home/user/app-deployment/server-list.txt | awk 'BEGIN{print "Hostname,Version"}{print}' > /home/user/app-deployment/host-version-report.csv
sed -i 's/DEPLOY START/DEPLOY INITIATED/g' /home/user/app-deployment/deployment.log
count=$(grep -c 'FAILED' /home/user/app-deployment/deployment.log); echo "$count"; echo "TOTAL_FAILED,$count" >> /home/user/app-deployment/host-version-report.csv
