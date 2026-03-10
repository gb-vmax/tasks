#!/bin/bash
set -e
cd /home/user

ls /home/user/server_data
du -k --max-depth=1 /home/user/server_data
{ echo "Disk Usage Report: /home/user/server_data"; printf '=%.0s' {1..42}; echo; du -k --max-depth=1 /home/user/server_data | awk '$2 != "/home/user/server_data" && $1 >= 50' | sort -rn | awk '{print $1 "K\t" $2}'; } > /home/user/disk_report.txt
cat /home/user/disk_report.txt
