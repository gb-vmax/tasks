#!/bin/bash
set -e
cd /home/user

awk '$3=="ERROR"{print $2}' /home/user/logs/microservice-app.log | sort | uniq -c | awk '{print $2, $1}' | sort > /home/user/logs/error_summary.txt
cat /home/user/logs/error_summary.txt
