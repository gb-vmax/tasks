#!/bin/bash
set -e
cd /home/user

head /home/user/finops/charges.csv
awk -F',' '{print $4}' /home/user/finops/charges.csv | sort | uniq -c | sort -k1,1rn -k2,2 > /home/user/finops/team_charge_counts.txt
cat /home/user/finops/team_charge_counts.txt
awk -F',' '{print $4}' /home/user/finops/charges.csv | sort | uniq -c | sort -k1,1rn -k2,2 | awk '{print $1, $2}' > /home/user/finops/team_charge_counts.txt
cat /home/user/finops/team_charge_counts.txt
