#!/bin/bash
set -e
cd /home/user

ls /home/user/cost_reports/
ls /home/user/cost_reports/subdir/
find /home/user/cost_reports -name "daily_*.csv" | xargs ls -la
find /home/user/cost_reports -name "daily_*.csv" -size +10k | xargs wc -c | awk '/total/{print $1}' > /home/user/cost_reports/savings_report.txt
cat /home/user/cost_reports/savings_report.txt
find /home/user/cost_reports -name "daily_*.csv" -size +10k | xargs rm
find /home/user/cost_reports -type f | xargs ls -la
