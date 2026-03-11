#!/bin/bash
set -e
cd /home/user

ls /home/user/diagnostics/
head -5 /home/user/diagnostics/access.log
head -5 /home/user/diagnostics/app.log
head -5 /home/user/diagnostics/syslog
wc -l /home/user/diagnostics/access.log /home/user/diagnostics/app.log /home/user/diagnostics/syslog
cat /home/user/diagnostics/access.log
cat /home/user/diagnostics/app.log
cat /home/user/diagnostics/syslog
cat /home/user/diagnostics/syslog | awk '{print $5}' | sed 's/\[.*//' | sed 's/://' | sort | uniq -c | sort -rn
python3 /dev/stdin << 'PYEOF'
import re
from collections import defaultdict

with open('/home/user/diagnostics/access.log') as f:
    access_lines = f.readlines()

total_requests = len(access_lines)
status_counts = defaultdict(int)
endpoint_counts = defaultdict(int)
total_bandwidth = 0

for line in access_lines:
    fields = line.split()
    status_counts[fields[8]] += 1
    endpoint_counts[fields[6]] += 1
    total_bandwidth += int(fields[9])

status_sorted = sorted(status_counts.items(), key=lambda x: int(x[0]))
endpoint_sorted = sorted(endpoint_counts.items(), key=lambda x: (-x[1], x[0]))[:3]

with open('/home/user/diagnostics/app.log') as f:
    app_lines = f.readlines()

level_counts = defaultdict(int)
error_messages = []
first_ts = None
last_ts = None

for line in app_lines:
    line = line.rstrip('\n')
    m = re.match(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (.*)$', line)
    if m:
        ts, level, msg = m.group(1), m.group(2), m.group(3)
        level_counts[level] += 1
        if level == 'ERROR':
            error_messages.append(msg)
        if first_ts is None:
            first_ts = ts
        last_ts = ts

with open('/home/user/diagnostics/syslog') as f:
    sys_lines = f.readlines()

process_counts = defaultdict(int)
error_line_count = 0

for line in sys_lines:
    if re.search(r'error|Error|ERROR', line):
        error_line_count += 1
    fields = line.split()
    proc_name = re.sub(r'\[.*', '', fields[4]).rstrip(':')
    process_counts[proc_name] += 1

unique_processes = len(process_counts)
top_procs = sorted(process_counts.items(), key=lambda x: (-x[1], x[0]))[:2]

lines = []
lines.append('=== DIAGNOSTICS REPORT ===')
lines.append('')
lines.append('--- ACCESS LOG ---')
lines.append('Total requests: {}'.format(total_requests))
lines.append('Status codes:')
for code, count in status_sorted:
    lines.append('  {}: {}'.format(code, count))
lines.append('Top endpoints:')
for path, count in endpoint_sorted:
    lines.append('  {}: {}'.format(path, count))
lines.append('Total bandwidth: {} bytes'.format(total_bandwidth))
lines.append('')
lines.append('--- APPLICATION LOG ---')
lines.append('Log levels:')
for level in sorted(level_counts.keys()):
    lines.append('  {}: {}'.format(level, level_counts[level]))
lines.append('Errors:')
for msg in error_messages:
    lines.append('  - {}'.format(msg))
lines.append('First log entry: {}'.format(first_ts))
lines.append('Last log entry: {}'.format(last_ts))
lines.append('')
lines.append('--- SYSTEM LOG ---')
lines.append('Unique processes: {}'.format(unique_processes))
lines.append('Error-related lines: {}'.format(error_line_count))
lines.append('Top processes:')
for proc, count in top_procs:
    lines.append('  {}: {}'.format(proc, count))

with open('/home/user/diagnostics/report.txt', 'w') as out:
    out.write('\n'.join(lines) + '\n')

print('Done')
PYEOF
cat /home/user/diagnostics/report.txt
xxd /home/user/diagnostics/report.txt | tail -3
od -c /home/user/diagnostics/report.txt | tail -3
