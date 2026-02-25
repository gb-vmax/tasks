#!/bin/bash
set -e
cd /home/user

awk '{print "[SCAN] "$0"\nPorts:\n80/tcp open\n443/tcp closed\n22/tcp open\nVulnerabilities:\nCVE-2021-1234: LOW\nCVE-2019-8903: HIGH\n---"}' /home/user/targets.txt > /home/user/vulnscan_results.txt
printf "Targets scanned: %d\nOpen ports found: %d\nVulnerability counts:\nCVE-2021-1234 (LOW): %d times\nCVE-2019-8903 (HIGH): %d times\n" "$(grep -c '^\[SCAN\]' /home/user/vulnscan_results.txt)" "$(grep 'tcp open' /home/user/vulnscan_results.txt | sort | uniq | wc -l)" "$(grep -c 'CVE-2021-1234: LOW' /home/user/vulnscan_results.txt)" "$(grep -c 'CVE-2019-8903: HIGH' /home/user/vulnscan_results.txt)" > /home/user/report_summary.log
cat /home/user/report_summary.log
