#!/bin/bash
set -e
cd /home/user

cat /home/user/logs/production.log
python3 << 'EOF'
import re

logfile = '/home/user/logs/production.log'
lines = open(logfile).readlines()

# Parse lines
parsed = []
for line in lines:
    line = line.rstrip('\n')
    m = re.match(r'\[(\S+)\] \[(\S+)\] \[(\S+)\] (.*)', line)
    if m:
        parsed.append({'ts': m.group(1), 'sev': m.group(2), 'svc': m.group(3), 'msg': m.group(4)})

# Section 1
ef_lines = [p for p in parsed if p['sev'] in ('ERROR', 'FATAL')]
earliest = min(p['ts'] for p in ef_lines)
latest = max(p['ts'] for p in ef_lines)

# Section 2
from collections import Counter
sev_counts = Counter(p['sev'] for p in parsed)

# Section 3
svc_counts = Counter(p['svc'] for p in ef_lines)
svc_sorted = sorted(svc_counts.items(), key=lambda x: (-x[1], x[0]))

# Section 4
err_counts = Counter()
for p in parsed:
    m = re.search(r'ERR-\d+', p['msg'])
    if m:
        err_counts[m.group()] += 1
err_sorted = sorted(err_counts.items(), key=lambda x: (-x[1], int(x[0].split('-')[1])))

# Section 5
payment_fatal = any(p['sev'] == 'FATAL' and p['svc'] == 'payment-service' for p in parsed)

report = []
report.append('=== INCIDENT TRIAGE REPORT ===')
report.append(f'Incident window: {earliest} to {latest}')
report.append('')
report.append('--- Severity Breakdown ---')
report.append(f'FATAL: {sev_counts.get("FATAL", 0)}')
report.append(f'ERROR: {sev_counts.get("ERROR", 0)}')
report.append(f'WARN: {sev_counts.get("WARN", 0)}')
report.append(f'INFO: {sev_counts.get("INFO", 0)}')
report.append('')
report.append('--- Affected Services (ERROR/FATAL only) ---')
for svc, cnt in svc_sorted:
    report.append(f'{svc}: {cnt}')
report.append('')
report.append('--- Error Code Frequency ---')
for code, cnt in err_sorted:
    report.append(f'{code}: {cnt}')
report.append('')
if payment_fatal:
    report.append('*** CRITICAL: payment-service has FATAL errors — escalate immediately ***')
else:
    report.append('payment-service: no FATAL errors detected')

with open('/home/user/logs/triage_report.txt', 'w') as f:
    f.write('\n'.join(report) + '\n')

print("Done")
EOF
cat /home/user/logs/triage_report.txt
cat -A /home/user/logs/triage_report.txt
