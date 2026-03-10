#!/bin/bash
set -e
cd /home/user

cat /home/user/metrics/service_latency.txt
{ printf "SERVICE\tENV\tP99\tRATIO\n"; awk -F'|' 'NR>1 && $5>100 { ratio=$5/$3; printf "%s\t%s\t%s\t%.1f\n", $1, $2, $5, ratio }' /home/user/metrics/service_latency.txt | sort -t$'\t' -k3 -rn; } > /home/user/metrics/high_latency.txt
cat /home/user/metrics/high_latency.txt
sed -i 's/production/prod/g; s/staging/stg/g' /home/user/metrics/high_latency.txt
cat /home/user/metrics/high_latency.txt
