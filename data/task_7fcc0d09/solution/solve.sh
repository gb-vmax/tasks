#!/bin/bash
set -e
cd /home/user

head -20 /home/user/logs/access.log
grep -P '"[A-Z]+ /api/[^ ]* HTTP/[0-9.]+" 404 ' /home/user/logs/access.log > /home/user/logs/api_404s.log
cat /home/user/logs/api_404s.log
N=$(wc -l < /home/user/logs/api_404s.log); M=$(awk '{print $1}' /home/user/logs/api_404s.log | sort -u | wc -l); printf "Total 404s on /api/: %s\nUnique IPs: %s\n" "$N" "$M" > /home/user/logs/api_404_summary.txt
cat /home/user/logs/api_404_summary.txt
