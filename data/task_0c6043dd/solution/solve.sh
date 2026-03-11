#!/bin/bash
set -e
cd /home/user

cat /home/user/data/sales.csv
awk -F',' 'NR>1 { revenue[$2] += $4 * $5 } END { for (cat in revenue) print cat ": " int(revenue[cat]) }' /home/user/data/sales.csv | sort > /home/user/data/category_revenue.txt
cat /home/user/data/category_revenue.txt
