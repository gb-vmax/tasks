#!/bin/bash
set -e
cd /home/user

head -5 /home/user/logs/fw_deny.log
grep -oP 'src=\K[^ ]+' /home/user/logs/fw_deny.log | sort | uniq -c | sort -k1,1rn -k2,2r | awk '{print $1, $2}' > /home/user/logs/deny_count.txt
cat /home/user/logs/deny_count.txt
grep -oP 'src=\K[^ ]+' /home/user/logs/fw_deny.log | sort | uniq -c
