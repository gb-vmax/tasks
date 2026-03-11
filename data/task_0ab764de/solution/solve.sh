#!/bin/bash
set -e
cd /home/user

awk '$6 > 400 { printf "[%s] %s %s => %sms (%s)\n", $1, $3, $4, $6, $5 }' /home/user/logs/access.log > /home/user/logs/slow_requests.txt
cat /home/user/logs/slow_requests.txt
