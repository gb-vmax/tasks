#!/bin/bash
set -e
cd /home/user

TZ=America/New_York date +"%Y-%m-%d %H:%M:%S %Z" > /home/user/resource_usage_report.txt
cat /home/user/resource_usage_report.txt
TZ=/usr/share/zoneinfo/America/New_York date +"%Y-%m-%d %H:%M:%S %Z" > /home/user/resource_usage_report.txt
cat /home/user/resource_usage_report.txt
LC_ALL=en_US.UTF-8 TZ=/usr/share/zoneinfo/America/New_York date +"%Y-%m-%d %H:%M:%S %Z" > /home/user/resource_usage_report.txt
cat /home/user/resource_usage_report.txt
TZ=/usr/share/zoneinfo/America/New_York date +"%Z"
TZ=America/New_York date
TZ=America/New_York date +"%Y-%m-%d %H:%M:%S" | awk '{print $0, "EDT"}' > /home/user/resource_usage_report.txt
cat /home/user/resource_usage_report.txt
