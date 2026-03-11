#!/bin/bash
set -e
cd /home/user

cat /home/user/finops/resources.csv
python3 -c "
import csv
from collections import defaultdict

costs = defaultdict(float)

with open('/home/user/finops/resources.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        costs[row['service']] += float(row['monthly_cost_usd'])

services = sorted(costs.keys())
grand_total = sum(costs[s] for s in services)

lines = []
lines.append('Monthly Cost Summary')
lines.append('====================')
for s in services:
    lines.append(f'{s}: \${costs[s]:.2f}')
lines.append('====================')
lines.append(f'Total: \${grand_total:.2f}')

with open('/home/user/finops/cost_summary.txt', 'w') as f:
    f.write('\n'.join(lines) + '\n')

print('Done')
"
cat /home/user/finops/cost_summary.txt
