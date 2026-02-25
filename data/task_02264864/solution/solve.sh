#!/bin/bash
set -e
cd /home/user

sort /home/user/backup/logins.log | uniq -c | sort -k1,1nr -k2,2 | awk '{print $1, $2}' > /home/user/backup/login_frequencies.txt
cat /home/user/backup/login_frequencies.txt
