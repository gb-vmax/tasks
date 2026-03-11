#!/bin/bash
set -e
cd /home/user

cat /home/user/containers/stats.txt
python3 -c "
import re

with open('/home/user/containers/stats.txt', 'r') as f:
    lines = f.readlines()

header = lines[0]
data_lines = lines[1:]

max_mem_pct = -1
top_name = ''
top_mem_usage = ''
top_mem_pct_str = ''

for line in data_lines:
    line = line.strip()
    if not line:
        continue
    # Split by multiple spaces
    parts = re.split(r'\s{2,}', line)
    # columns: CONTAINER_ID, NAME, CPU%, MEM_USAGE/LIMIT, MEM%, NET_I/O, BLOCK_I/O
    container_id = parts[0]
    name = parts[1]
    cpu_pct = parts[2]
    mem_usage = parts[3]
    mem_pct_str = parts[4]
    mem_pct = float(mem_pct_str.replace('%', ''))
    if mem_pct > max_mem_pct:
        max_mem_pct = mem_pct
        top_name = name
        top_mem_usage = mem_usage
        top_mem_pct_str = mem_pct_str

if max_mem_pct >= 80:
    recommendation = 'ACTION REQUIRED: Increase memory limit or scale horizontally.'
elif max_mem_pct >= 50:
    recommendation = 'WARNING: Monitor closely and consider increasing memory limit.'
else:
    recommendation = 'OK: Memory usage is within acceptable range.'

report = (
    'Container Memory Optimization Report\n'
    '=====================================\n'
    f'Top memory consumer: {top_name}\n'
    f'Memory usage: {top_mem_usage}\n'
    f'Memory percent: {top_mem_pct_str}\n'
    f'Recommendation: {recommendation}\n'
)

with open('/home/user/containers/report.txt', 'w') as f:
    f.write(report)

print(report, end='')
"
cat /home/user/containers/report.txt
cat -A /home/user/containers/report.txt
xxd /home/user/containers/report.txt | tail -5
wc -c /home/user/containers/report.txt && od -c /home/user/containers/report.txt | tail -5
