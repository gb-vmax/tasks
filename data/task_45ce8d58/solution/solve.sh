#!/bin/bash
set -e
cd /home/user

ls /home/user/data/quarterly/ /home/user/data/customers/ 2>/dev/null || echo "Directories not found"
mkdir -p /home/user/workspace/
ln -s /home/user/data/quarterly/q1_sales_data.csv /home/user/workspace/sales_q1.csv && ln -s /home/user/data/quarterly/q2_sales_data.csv /home/user/workspace/sales_q2.csv && ln -s /home/user/data/customers/master_customers.csv /home/user/workspace/customers.csv
printf 'sales_q1.csv -> /home/user/data/quarterly/q1_sales_data.csv\nsales_q2.csv -> /home/user/data/quarterly/q2_sales_data.csv\ncustomers.csv -> /home/user/data/customers/master_customers.csv\n' > /home/user/workspace/manifest.txt
ls -la /home/user/workspace/ && echo "---" && cat /home/user/workspace/manifest.txt
