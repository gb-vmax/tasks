#!/bin/bash
set -e
cd /home/user

head -5 /home/user/data/sales.csv
awk -F',' 'BEGIN{OFS=","} {print $2,$3,$8}' /home/user/data/sales.csv > /home/user/data/sales_report.csv
cat /home/user/data/sales_report.csv
