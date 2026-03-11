#!/bin/bash
set -e
cd /home/user

cat /home/user/finops/aws_costs.csv
awk -F',' 'BEGIN{OFS=","} {print $6,$3,$1,$2,$4,$5}' /home/user/finops/aws_costs.csv > /home/user/finops/aws_costs_reordered.csv
cat /home/user/finops/aws_costs_reordered.csv
