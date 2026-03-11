#!/bin/bash
set -e
cd /home/user

cat /home/user/legacy/service_inventory.py
mkdir -p /home/user/migration && python3 /home/user/legacy/service_inventory.py > /home/user/migration/inventory_raw.txt
grep 'STATUS=active' /home/user/migration/inventory_raw.txt > /home/user/migration/active_services.txt
echo "TOTAL_ACTIVE=$(wc -l < /home/user/migration/active_services.txt)" >> /home/user/migration/active_services.txt
cat /home/user/migration/active_services.txt
cat /home/user/migration/inventory_raw.txt
