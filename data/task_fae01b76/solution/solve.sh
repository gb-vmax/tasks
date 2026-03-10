#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/audit && awk -F: '$3 >= 1000 && $3 != 65534 {print $3 "\t" $1 "\t" $6 "\t" $7}' /etc/passwd | sort -n | awk -F'\t' 'BEGIN{print "=== USER ACCOUNT AUDIT REPORT ==="; print "Generated from: /etc/passwd"; print ""; print "Non-system accounts (UID >= 1000):"} {printf "  %s | UID: %s | Home: %s | Shell: %s\n", $2, $1, $3, $4; count++} END{print ""; print "Total non-system accounts: " count}' > /home/user/audit/user_accounts.txt
cat /home/user/audit/user_accounts.txt
