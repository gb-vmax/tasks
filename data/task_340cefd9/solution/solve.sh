#!/bin/bash
set -e
cd /home/user

grep '^ERROR' /home/user/logs/app.log > /home/user/logs/error_lines.log
grep -E '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' /home/user/logs/app.log > /home/user/logs/ip_lines.log
echo -e "error_lines.log: $(wc -l < /home/user/logs/error_lines.log) lines\nip_lines.log: $(wc -l < /home/user/logs/ip_lines.log) lines" > /home/user/logs/regex_summary.log
cat /home/user/logs/regex_summary.log
