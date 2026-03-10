#!/bin/bash
set -e
cd /home/user

cat /home/user/policy/benchmark.json
cat /home/user/policy/scan_results.json
python3 -c "
import json

with open('/home/user/policy/benchmark.json') as f:
    benchmarks = json.load(f)

with open('/home/user/policy/scan_results.json') as f:
    scan_results = json.load(f)

# Build lookup for scan results
scan_map = {entry['control_id']: entry['value'] for entry in scan_results}

results = []
passed = 0
failed = 0

for control in benchmarks:
    cid = control['control_id']
    desc = control['description']
    threshold = control['threshold']
    operator = control['operator']
    value = scan_map[cid]

    if operator == 'lte':
        ok = value <= threshold
    elif operator == 'gte':
        ok = value >= threshold

    if ok:
        status = 'PASS'
        passed += 1
    else:
        status = 'FAIL'
        failed += 1

    results.append((status, cid, desc, operator, threshold, value))

total = passed + failed
compliance = round((passed / total) * 100)
overall = 'COMPLIANT' if failed == 0 else 'NON-COMPLIANT'

lines = []
lines.append('=== SECURITY BENCHMARK COMPLIANCE REPORT ===')
lines.append('')
lines.append('CONTROL RESULTS:')
for status, cid, desc, operator, threshold, value in results:
    lines.append(f'  [{status}] {cid}: {desc} (expected {operator} {int(threshold)}, got {int(value)})')
lines.append('')
lines.append('SUMMARY:')
lines.append(f'Total controls: {total}')
lines.append(f'Passed: {passed}')
lines.append(f'Failed: {failed}')
lines.append(f'Compliance: {compliance}%')
lines.append('')
lines.append(f'OVERALL STATUS: {overall}')

with open('/home/user/policy/compliance_report.txt', 'w') as f:
    f.write('\n'.join(lines) + '\n')

print('Report written successfully.')
"
cat /home/user/policy/compliance_report.txt
