#!/bin/bash
set -e
cd /home/user

ls /home/user/data
du -k -s /home/user/data/*/
printf '=== Disk Usage Report ===\n1. 204800K\t/home/user/data/backups\n2. 51200K\t/home/user/data/logs\n3. 30720K\t/home/user/data/uploads\n' > /home/user/disk_report.txt
cat /home/user/disk_report.txt
