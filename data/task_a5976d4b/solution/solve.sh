#!/bin/bash
set -e
cd /home/user

sort /home/user/pentest/scan_results.txt | uniq -c | sort -k1,1rn -k2,2 | awk '{print $1, $2}' > /home/user/pentest/vuln_summary.txt
cat /home/user/pentest/vuln_summary.txt
