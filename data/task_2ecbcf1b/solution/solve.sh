#!/bin/bash
set -e
cd /home/user

cat /home/user/servers/inventory.json
jq -r '(["hostname","ip_address","cpu_cores","ram_gb","status"] | join(",")), (sort_by(.hostname)[] | [.hostname, .ip_address, .cpu_cores, .ram_gb, .status] | join(","))' /home/user/servers/inventory.json > /home/user/servers/report.csv
python3 -c "
import json, csv

with open('/home/user/servers/inventory.json') as f:
    servers = json.load(f)

fields = ['hostname', 'ip_address', 'cpu_cores', 'ram_gb', 'status']
servers_sorted = sorted(servers, key=lambda x: x['hostname'])

with open('/home/user/servers/report.csv', 'w', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONE)
    writer.writerow(fields)
    for s in servers_sorted:
        writer.writerow([s[field] for field in fields])
"
cat /home/user/servers/report.csv
