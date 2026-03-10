#!/bin/bash
set -e
cd /home/user

cat /home/user/data/sales.psv
awk -F'|' 'NR>1 { total = $4 * $5; printf "%s|%s|%s|%s|%.2f\n", $1, $2, $3, $4, total }' /home/user/data/sales.psv > /home/user/data/sales_totals.psv
cat /home/user/data/sales_totals.psv
sed 's/\([^|]*\)|\([^|]*\)|\([^|]*\)|\([^|]*\)|\([^|]*\)/[\1] \2 sold \4 units of \3 for $\5/' /home/user/data/sales_totals.psv > /home/user/data/sales_report.txt
cat /home/user/data/sales_report.txt
awk -F'|' '{ sum += $5 } END { printf "GRAND TOTAL: $%.2f\n", sum }' /home/user/data/sales_totals.psv >> /home/user/data/sales_report.txt
cat /home/user/data/sales_report.txt
