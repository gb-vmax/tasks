#!/bin/bash
set -e
cd /home/user

cat /home/user/logs/auth.log
python3 << 'EOF'
import re
from collections import defaultdict

log_file = '/home/user/logs/auth.log'
report_file = '/home/user/reports/audit_report.txt'

import os
os.makedirs('/home/user/reports', exist_ok=True)

counts = defaultdict(int)

with open(log_file) as f:
    for line in f:
        m = re.search(r'Failed password for (?:invalid user )?(\S+) from', line)
        if m:
            counts[m.group(1)] += 1

total = sum(counts.values())

# Sort by count descending, then alphabetically
sorted_users = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

high_risk = sorted(u for u, c in counts.items() if c >= 3)

with open(report_file, 'w') as f:
    f.write('=== FAILED LOGIN AUDIT REPORT ===\n')
    f.write(f'Log file: {log_file}\n')
    f.write(f'Total failed attempts: {total}\n')
    f.write('\n')
    f.write('Failed attempts per user (descending):\n')
    for user, count in sorted_users:
        f.write(f'  {user}: {count}\n')
    f.write('\n')
    f.write('Users with 3 or more failed attempts (HIGH RISK):\n')
    if high_risk:
        for user in high_risk:
            f.write(f'  {user}\n')
    else:
        f.write('  (none)\n')

print("Done")
EOF
cat /home/user/reports/audit_report.txt
