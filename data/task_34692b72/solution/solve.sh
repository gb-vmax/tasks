#!/bin/bash
set -e
cd /home/user

cat /home/user/analysis/scan_log.py
cd /home/user/analysis && python3 scan_log.py 2>/dev/null | grep '^SUSPICIOUS' | awk '{print $2}' | sort -u > /tmp/unique_ips.txt && echo "Done"
count=$(wc -l < /tmp/unique_ips.txt) && { echo "Suspicious IPs found: $count"; cat /tmp/unique_ips.txt; } > /home/user/analysis/report.txt && cat /home/user/analysis/report.txt
