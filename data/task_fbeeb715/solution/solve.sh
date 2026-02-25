#!/bin/bash
set -e
cd /home/user

(head -n1 /home/user/creds/users.csv && paste -d, <(tail -n +2 /home/user/creds/users.csv | cut -d',' -f1-3) /home/user/creds/new_keys.txt) > /home/user/creds/users_rotated.csv
{ [ -f /home/user/creds/users_rotated.csv ] && echo "users_rotated.csv exists"; \
[ "$(head -n1 /home/user/creds/users_rotated.csv | awk -F, '{print NF}')" -eq 4 ] && echo "4 columns in header"; \
comm -23 <(tail -n +2 /home/user/creds/users_rotated.csv | cut -d',' -f4 | sort) <(sort /home/user/creds/new_keys.txt | uniq -u) | grep -q '^' && echo "All api_keys are new"; \
echo "Row count: $(($(wc -l < /home/user/creds/users_rotated.csv)-1))"; } > /home/user/creds/rotation_check.log
cat /home/user/creds/users_rotated.csv /home/user/creds/rotation_check.log
{ [ -f /home/user/creds/users_rotated.csv ] && echo "users_rotated.csv exists"; \
[ "$(head -n1 /home/user/creds/users_rotated.csv | awk -F, '{print NF}')" -eq 4 ] && echo "4 columns in header"; \
paste -d' ' <(tail -n +2 /home/user/creds/users_rotated.csv | cut -d',' -f4) /home/user/creds/new_keys.txt | awk '$1!=$2{exit 1} END{if(NR>0) print "All api_keys are new"}'; \
echo "Row count: $(($(wc -l < /home/user/creds/users_rotated.csv)-1))"; } > /home/user/creds/rotation_check.log
cat /home/user/creds/rotation_check.log
