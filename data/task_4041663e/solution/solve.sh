#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/logs && printf "2024-04-11 10:12:01 INFO Starting application\n2024-04-11 10:12:03 WARNING Deprecated configuration detected\n2024-04-11 10:12:07 ERROR Failed to connect to database\n2024-04-11 10:12:09 INFO Database retry attempt 1\n2024-04-11 10:12:11 WARNING Low disk space\n2024-04-11 10:12:13 ERROR Could not locate config file\n2024-04-11 10:12:16 INFO Application shutdown complete\n" > /home/user/logs/testapp.log
grep -Ew 'WARNING|ERROR' /home/user/logs/testapp.log > /home/user/logs/filtered_report.txt
echo /home/user/logs/filtered_report.txt
