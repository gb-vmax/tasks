#!/bin/bash
set -e
cd /home/user

awk -F, 'NR>1 && $2 !~ /^registry\.corporate\.com\// {print "{\"container_name\": \"" $1 "\", \"image_source\": \"" $2 "\", \"compliance\": \"FAIL\"}"}' /home/user/containers/inventory.csv | jq -s '.' > /home/user/output/policy_report.json
awk -F, 'NR>1 && $2 !~ /^registry\.corporate\.com\// {printf "%s{\"container_name\": \"%s\", \"image_source\": \"%s\", \"compliance\": \"FAIL\"}", (n++?",\n":"\n  "), $1, $2} END {if(n) print "\n";}' /home/user/containers/inventory.csv | { echo '[' > /home/user/output/policy_report.json; cat >> /home/user/output/policy_report.json; echo ']' >> /home/user/output/policy_report.json; }
cat /home/user/output/policy_report.json
