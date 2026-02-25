#!/bin/bash
set -e
cd /home/user

awk '{print $1}' /home/user/logs/access.log | sort | uniq > /home/user/diagnostics/unique_ips.txt
sed -i 's/404/NOT_FOUND/g' /home/user/logs/access.log
awk '{count[$9]++} END {for (c in count) print c ": " count[c]}' /home/user/logs/access.log | sort > /home/user/diagnostics/http_status_count.txt
cat /home/user/diagnostics/unique_ips.txt
grep 404 /home/user/logs/access.log
cat /home/user/diagnostics/http_status_count.txt
