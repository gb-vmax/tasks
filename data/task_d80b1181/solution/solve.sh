#!/bin/bash
set -e
cd /home/user

cat /home/user/observability/dashboards.json
python3 -c "
import json

with open('/home/user/observability/dashboards.json') as f:
    data = json.load(f)

lines = []
for d in data['dashboards']:
    name = d['name']
    status = d['status']
    has_threshold = 'threshold' in d
    threshold = d['threshold'] if has_threshold else 'MISSING'
    
    if status == 'error' or not has_threshold:
        lines.append(f'[NEEDS REPAIR] {name} | status={status} | threshold={threshold}')

report = '\n'.join(lines) + '\n\nTotal dashboards needing repair: ' + str(len(lines)) + '\n'

with open('/home/user/observability/repair_report.txt', 'w') as f:
    f.write(report)

print(report, end='')
"
cat /home/user/observability/repair_report.txt
