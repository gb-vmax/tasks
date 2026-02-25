#!/bin/bash
set -e
cd /home/user

cut -d, -f3,4 /home/user/backup/backup_report.csv > /home/user/backup/verification_output.csv
cat /home/user/backup/verification_output.csv
