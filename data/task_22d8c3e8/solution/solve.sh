#!/bin/bash
set -e
cd /home/user

cat /home/user/infra/servers.csv
awk -F',' 'NR>1 && $3=="prod" && $4=="unprovisioned" {print $1}' /home/user/infra/servers.csv | { echo "[provision_targets]"; cat; } > /home/user/infra/provision_targets.ini
cat /home/user/infra/provision_targets.ini
