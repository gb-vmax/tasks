#!/bin/bash
set -e
cd /home/user

cat /home/user/capacity/analyze_usage.py
python3 /home/user/capacity/analyze_usage.py /home/user/capacity/server_metrics.csv
cat /home/user/capacity/server_metrics.csv
python3 /home/user/capacity/analyze_usage.py /home/user/capacity/server_metrics.csv | python3 -c "
import sys

lines = sys.stdin.read().splitlines()
data = {}
for line in lines:
    if line.startswith('Hosts analyzed:'):
        data['hosts'] = line.split(': ')[1]
    elif line.startswith('Average CPU usage:'):
        data['cpu'] = line.split(': ')[1].rstrip('%')
    elif line.startswith('Average MEM usage:'):
        data['mem'] = line.split(': ')[1].rstrip('%')
    elif line.startswith('Average DISK usage:'):
        data['disk'] = line.split(': ')[1].rstrip('%')
    elif line.startswith('High CPU hosts (>80%):'):
        val = line.split(': ', 1)[1]
        if val == 'none':
            data['high_cpu'] = 'none'
        else:
            data['high_cpu'] = ', '.join(sorted(val.split(', ')))
    elif line.startswith('High MEM hosts (>80%):'):
        val = line.split(': ', 1)[1]
        if val == 'none':
            data['high_mem'] = 'none'
        else:
            data['high_mem'] = ', '.join(sorted(val.split(', ')))

report = f'''=== Capacity Report ===
Hosts analyzed: {data['hosts']}
CPU avg: {data['cpu']}%
MEM avg: {data['mem']}%
DISK avg: {data['disk']}%
High CPU hosts (>80%): {data['high_cpu']}
High MEM hosts (>80%): {data['high_mem']}'''

with open('/home/user/capacity/report.txt', 'w') as f:
    f.write(report + '\n')
print(report)
"
cat /home/user/capacity/report.txt
