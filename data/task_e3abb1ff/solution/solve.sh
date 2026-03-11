#!/bin/bash
set -e
cd /home/user

cat /home/user/iot/devices.csv
awk -F',' 'NR>1 {print $4 ":" $1 ":" $3}' /home/user/iot/devices.csv > /home/user/iot/deploy_targets.csv
cat /home/user/iot/deploy_targets.csv
