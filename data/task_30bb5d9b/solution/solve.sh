#!/bin/bash
set -e
cd /home/user

cat /home/user/monitoring/metrics.csv
python3 << 'EOF'
import csv
from collections import defaultdict

data = defaultdict(list)

with open('/home/user/monitoring/metrics.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        key = (row['server'], row['metric'])
        data[key].append(float(row['value']))

def format_max(val):
    # Preserve as it appears: integer if no decimal part, else with decimal digits
    if val == int(val):
        return str(int(val)) + '.0'
    else:
        return str(val)

sections = []
for key in sorted(data.keys()):
    server, metric = key
    values = data[key]
    max_val = max(values)
    avg_val = round(sum(values) / len(values), 2)
    threshold = round(avg_val + 0.20 * (max_val - avg_val), 2)
    
    section = f"[{server}:{metric}]\nmax={format_max(max_val)}\navg={avg_val}\nthreshold={threshold}"
    sections.append(section)

output = '\n\n'.join(sections)

with open('/home/user/monitoring/alert_thresholds.cfg', 'w') as f:
    f.write(output)

print("Done. Output:")
print(output)
EOF
cat /home/user/monitoring/alert_thresholds.cfg
