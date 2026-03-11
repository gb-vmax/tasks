#!/bin/bash
set -e
cd /home/user

cat /home/user/devsecops/accounts.json
python3 -c "
import json

with open('/home/user/devsecops/accounts.json') as f:
    accounts = json.load(f)

violations = [a for a in accounts if a.get('password_expires') is False]

lines = []
lines.append('POLICY VIOLATION REPORT')
lines.append('=======================')
lines.append('NON-COMPLIANT ACCOUNTS (password_expires=false):')
lines.append('')
for a in violations:
    lines.append(f\"{a['name']} | role={a['role']} | env={a['env']}\")
lines.append('')
lines.append(f'Total violations: {len(violations)}')

with open('/home/user/devsecops/violations.txt', 'w') as f:
    f.write('\n'.join(lines) + '\n')
"
cat /home/user/devsecops/violations.txt
