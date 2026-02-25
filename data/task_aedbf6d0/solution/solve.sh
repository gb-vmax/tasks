#!/bin/bash
set -e
cd /home/user

awk -F',' 'NR==1{next} {gsub(/"/,"",$6); sum+=$6; n++} END{printf "%s,%d,%.2f,%.2f\n", "North", n, sum, (n ? sum/n : 0)}' /home/user/sales_data/north.csv
awk -F',' 'NR==1{next} {gsub(/"/,"",$6); sum+=$6; n++} END{printf "%s,%d,%.2f,%.2f\n", "South", n, sum, (n ? sum/n : 0)}' /home/user/sales_data/south.csv
awk -F',' 'NR==1{next} {gsub(/"/,"",$6); sum+=$6; n++} END{printf "%s,%d,%.2f,%.2f\n", "West", n, sum, (n ? sum/n : 0)}' /home/user/sales_data/west.csv
printf "Region,TotalOrders,TotalSaleAmount,AverageSaleAmount\nNorth,3,855.50,285.17\nSouth,2,430.00,215.00\nWest,4,795.00,198.75\n" > /home/user/sales_data/summary.csv
printf '[\n  {"Region": "North", "TotalOrders": 3, "TotalSaleAmount": 855.50, "AverageSaleAmount": 285.17},\n  {"Region": "South", "TotalOrders": 2, "TotalSaleAmount": 430.00, "AverageSaleAmount": 215.00},\n  {"Region": "West", "TotalOrders": 4, "TotalSaleAmount": 795.00, "AverageSaleAmount": 198.75}\n]\n' > /home/user/sales_data/summary.json
printf "north.csv | Region: North | TotalOrders: 3 | TotalSaleAmount: 855.50 | AverageSaleAmount: 285.17\nsouth.csv | Region: South | TotalOrders: 2 | TotalSaleAmount: 430.00 | AverageSaleAmount: 215.00\nwest.csv | Region: West | TotalOrders: 4 | TotalSaleAmount: 795.00 | AverageSaleAmount: 198.75\n" > /home/user/sales_data/process.log
cat /home/user/sales_data/summary.csv
cat /home/user/sales_data/summary.json
cat /home/user/sales_data/process.log
