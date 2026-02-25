#!/bin/bash
set -e
cd /home/user

awk -F'; ' '/status: running/ { for(i=1;i<=NF;i++) { if($i ~ /^name:/) { split($i,a,": "); name=a[2] } if($i ~ /^image:/) { split($i,b,": "); image=b[2] } } print name "," image }' /home/user/logs/service_status.log > /home/user/logs/running_containers.csv
cat /home/user/logs/running_containers.csv
