#!/bin/bash
set -e
cd /home/user

cat /home/user/data/sales.csv
awk -F',' 'NR==1 || $5 > 5000' /home/user/data/sales.csv > /home/user/data/high_revenue.csv && cat /home/user/data/high_revenue.csv
sed -e 's/region,category,month,units_sold,revenue/REGION,CATEGORY,MONTH,UNITS_SOLD,REVENUE/' -e 's/North/Northern/g' -e 's/South/Southern/g' /home/user/data/high_revenue.csv > /home/user/data/report.txt && cat /home/user/data/report.txt
echo "=== high_revenue.csv ===" && cat /home/user/data/high_revenue.csv && echo "" && echo "=== report.txt ===" && cat /home/user/data/report.txt
