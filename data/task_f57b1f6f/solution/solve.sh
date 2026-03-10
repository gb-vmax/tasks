#!/bin/bash
set -e
cd /home/user

cat /home/user/deployments/rollout_2024.log
python3 -c "
import re

log_file = '/home/user/deployments/rollout_2024.log'
report_file = '/home/user/deployments/rollout_report.txt'

services = {}

with open(log_file) as f:
    for line in f:
        line = line.strip()
        m = re.search(r'SERVICE=(\S+)\s+ACTION=(\S+)\s+STATUS=(\S+)\s+DURATION_MS=(\S+)', line)
        if m:
            name, action, status, duration = m.groups()
            if action == 'END':
                services[name] = {'status': status, 'duration': int(duration)}

total = len(services)
successful = sum(1 for s in services.values() if s['status'] == 'success')
failed = total - successful

sorted_services = sorted(services.items())
fastest = min(services.items(), key=lambda x: x[1]['duration'])
slowest = max(services.items(), key=lambda x: x[1]['duration'])
avg = round(sum(s['duration'] for s in services.values()) / total)
failed_services = sorted(name for name, s in services.items() if s['status'] == 'failed')

with open(report_file, 'w') as f:
    f.write('=== DEPLOYMENT ROLLOUT REPORT ===\n')
    f.write(f'Log file: {log_file}\n')
    f.write(f'Total services deployed: {total}\n')
    f.write(f'Successful: {successful}\n')
    f.write(f'Failed: {failed}\n')
    f.write('\n')
    f.write('=== SERVICE DETAILS ===\n')
    for name, s in sorted_services:
        label = 'SUCCESS' if s['status'] == 'success' else 'FAILED'
        f.write(f'{name} [{label}] {s[\"duration\"]}ms\n')
    f.write('\n')
    f.write('=== TIMING STATISTICS ===\n')
    f.write(f'Fastest deployment: {fastest[0]} ({fastest[1][\"duration\"]}ms)\n')
    f.write(f'Slowest deployment: {slowest[0]} ({slowest[1][\"duration\"]}ms)\n')
    f.write(f'Average deployment time: {avg}ms\n')
    f.write('\n')
    f.write('=== FAILED SERVICES ===\n')
    if failed_services:
        for name in failed_services:
            f.write(f'{name}\n')
    else:
        f.write('None\n')
"
cat /home/user/deployments/rollout_report.txt
