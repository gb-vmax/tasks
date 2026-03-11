#!/bin/bash
set -e
cd /home/user

cat /home/user/data/sales.csv
awk -F',' 'NR==1 {print "transaction_id,date,amount,status"; next} $4 ~ /^PRD-[0-9]{3}$/ && ($6 == "completed" || $6 == "refunded") {print $1","$2","$5","$6}' /home/user/data/sales.csv > /home/user/data/filtered_sales.csv
cat /home/user/data/filtered_sales.csv
cat -A /home/user/data/sales.csv | head -3
awk -F',' 'NR>1 {print NR, $4, "|"$6"|"}' /home/user/data/sales.csv | head -5
awk -F',' 'NR>1 && $4 ~ /^PRD-[0-9]{3}$/ {print NR, $4, $6}' /home/user/data/sales.csv
awk -F',' 'NR>1 && $4 ~ /^PRD-[0-9][0-9][0-9]$/ {print NR, $4, $6}' /home/user/data/sales.csv
awk -F',' 'NR==1 {print "transaction_id,date,amount,status"; next} $4 ~ /^PRD-[0-9][0-9][0-9]$/ && ($6 == "completed" || $6 == "refunded") {print $1","$2","$5","$6}' /home/user/data/sales.csv > /home/user/data/filtered_sales.csv
cat /home/user/data/filtered_sales.csv
