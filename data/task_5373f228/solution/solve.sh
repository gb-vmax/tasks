#!/bin/bash
set -e
cd /home/user

cat /home/user/data/services.json
python3 -c "
import json, csv, io

with open('/home/user/data/services.json') as f:
    services = json.load(f)

fields = ['id', 'name', 'status', 'response_time_ms']
rows = [[str(s[field]) for field in fields] for s in services]

output = ','.join(fields) + '\n' + '\n'.join(','.join(row) for row in rows)

with open('/home/user/data/services_report.csv', 'w', newline='') as f:
    f.write(output)
"
cat /home/user/data/services_report.csv
xxd /home/user/data/services_report.csv | tail -3
od -c /home/user/data/services_report.csv | tail -3
