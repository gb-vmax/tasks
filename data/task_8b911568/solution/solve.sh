#!/bin/bash
set -e
cd /home/user

ls /home/user/archive
du -sk /home/user/archive/*/ | sort -rn | awk '{sub(/\/$/, "", $2); print $1 "K\t" $2}' > /home/user/disk_report.txt
cat /home/user/disk_report.txt
