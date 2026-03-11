#!/bin/bash
set -e
cd /home/user

cat /home/user/servers/inventory.csv
awk -F',' 'NR > 1 && $4 == "active" { printf "[%s] %s (%s)\n", $1, $2, $3 }' /home/user/servers/inventory.csv > /home/user/servers/active_servers.txt
cat /home/user/servers/active_servers.txt
