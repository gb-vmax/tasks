#!/bin/bash
set -euo pipefail

CONFIG_DIR="/home/user/opt_solver/configs"
DEPLOY_LOG="/home/user/opt_solver/deploy.log"

# Backup solver.conf
cp "${CONFIG_DIR}/solver.conf" "${CONFIG_DIR}/solver.conf.bak"

# Update max_iterations from 1000 to 2000
sed -i 's/max_iterations = 1000/max_iterations = 2000/' "${CONFIG_DIR}/solver.conf"

# Append log entry with timestamp
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
echo "[${TIMESTAMP}] solver.conf updated: max_iterations set to 2000 and backup created as solver.conf.bak" >> "${DEPLOY_LOG}"
