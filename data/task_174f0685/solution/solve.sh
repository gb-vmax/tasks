#!/bin/bash
set -e
cd /home/user

ls /home/user/finops/reports/
ls /home/user/finops/reports/2024-06/
ln -s /home/user/finops/reports/2024-06/aws_costs_2024-06.csv /home/user/finops/reports/current/aws.csv
ln -s /home/user/finops/reports/2024-06/gcp_costs_2024-06.csv /home/user/finops/reports/current/gcp.csv
ln -s /home/user/finops/reports/2024-06/azure_costs_2024-06.csv /home/user/finops/reports/current/azure.csv
printf 'aws.csv -> /home/user/finops/reports/2024-06/aws_costs_2024-06.csv\nazure.csv -> /home/user/finops/reports/2024-06/azure_costs_2024-06.csv\ngcp.csv -> /home/user/finops/reports/2024-06/gcp_costs_2024-06.csv\n' > /home/user/finops/reports/current/links_summary.txt
ls -la /home/user/finops/reports/current/ && echo "---" && cat /home/user/finops/reports/current/links_summary.txt
