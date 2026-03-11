#!/bin/bash
set -e
cd /home/user

cat /home/user/logs/uptime_monitor.log
grep -E 'status=(DOWN|TIMEOUT)' /home/user/logs/uptime_monitor.log > /home/user/logs/failed_checks.txt
wc -l < /home/user/logs/failed_checks.txt > /home/user/logs/failed_count.txt
cat /home/user/logs/failed_checks.txt
cat /home/user/logs/failed_count.txt
