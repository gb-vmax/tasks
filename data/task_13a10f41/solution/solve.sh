#!/bin/bash
set -e
cd /home/user

cat /home/user/security/firewall_deny.log | head -20
wc -l /home/user/security/firewall_deny.log
awk '{print $4}' /home/user/security/firewall_deny.log | sort | uniq -c | awk '{split($2,a,"."); printf "%s %s %03d%03d%03d%03d\n", $1, $2, a[1], a[2], a[3], a[4]}' | sort -k1,1rn -k3,3n | awk '{print $1, $2}' > /home/user/security/top_offenders.txt && echo "TOTAL_DENIES: $(wc -l < /home/user/security/firewall_deny.log)" >> /home/user/security/top_offenders.txt
cat /home/user/security/top_offenders.txt
