#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/triage/ && awk 'match($0, /"([^"]+)"/, req) && $(NF-1)=="404" { n++; split(req[1], a, " "); urls[a[2]] } END { print "404 count: " n; print "Unique URLs:"; for(u in urls) print u }' /home/user/logs/access.log > /home/user/triage/404_summary.txt
mkdir -p /home/user/triage/ && awk '$9 == 404 {count++; urls[$7]=1} END {print "404 count: " count; print "Unique URLs:"; for (u in urls) print u}' /home/user/logs/access.log > /home/user/triage/404_summary.txt
cat /home/user/triage/404_summary.txt
