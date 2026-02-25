#!/bin/bash
set -e
cd /home/user

python3 /home/user/etl_legacy/run_etl.py
cd /home/user/etl_legacy/ && python3 run_etl.py
cat /home/user/etl_legacy/sales_processed.csv
echo "$(date +%Y-%m-%dT%H:%M:%S)
ETL run completed successfully." > /home/user/etl_legacy/etl_run.log
cat /home/user/etl_legacy/etl_run.log
