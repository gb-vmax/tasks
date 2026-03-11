#!/bin/bash
set -e
cd /home/user

cat /home/user/security/auth.log
awk '{print $3}' /home/user/security/auth.log | sort | uniq -c | sort -k1,1rn -k2,2r | awk '{print $1, $2}' > /home/user/security/key_frequency.txt
cat /home/user/security/key_frequency.txt
