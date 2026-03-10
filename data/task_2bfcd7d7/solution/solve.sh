#!/bin/bash
set -e
cd /home/user

cat /home/user/configs/registry.json
python3 -c "
import json, csv

with open('/home/user/configs/registry.json') as f:
    data = json.load(f)

enabled = [d for d in data if d['enabled']]
enabled.sort(key=lambda x: x['service'])

with open('/home/user/configs/summary.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['service', 'env', 'version', 'last_modified'])
    for d in enabled:
        writer.writerow([d['service'], d['env'], d['version'], d['last_modified']])
"
cat /home/user/configs/summary.csv
cat -A /home/user/configs/summary.csv
python3 -c "
import json, csv

with open('/home/user/configs/registry.json') as f:
    data = json.load(f)

enabled = [d for d in data if d['enabled']]
enabled.sort(key=lambda x: x['service'])

with open('/home/user/configs/summary.csv', 'w', newline='') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['service', 'env', 'version', 'last_modified'])
    for d in enabled:
        writer.writerow([d['service'], d['env'], d['version'], d['last_modified']])
"
cat -A /home/user/configs/summary.csv
