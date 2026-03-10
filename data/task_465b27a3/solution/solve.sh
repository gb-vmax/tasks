#!/bin/bash
set -e
cd /home/user

cat /home/user/pipeline/build.log
python3 /tmp/gen_report.py
cat > /tmp/gen_report.py << 'PYEOF'
import re
from collections import defaultdict

log_path = '/home/user/pipeline/build.log'
report_path = '/home/user/pipeline/build_report.txt'

with open(log_path) as f:
    lines = f.readlines()

modules_order = []
module_status = {}
module_duration = {}
warnings = defaultdict(int)
errors = defaultdict(int)

for line in lines:
    line = line.strip()
    m = re.match(r'\[BUILD\] module=(\S+) status=(\S+) duration_ms=(\d+)', line)
    if m:
        name, status, dur = m.group(1), m.group(2), int(m.group(3))
        modules_order.append(name)
        module_status[name] = status
        module_duration[name] = dur
        continue
    m = re.match(r'\[WARN\] module=(\S+) ', line)
    if m:
        warnings[m.group(1)] += 1
        continue
    m = re.match(r'\[ERROR\] module=(\S+) ', line)
    if m:
        errors[m.group(1)] += 1

total_modules = len(modules_order)
passed = sum(1 for n in modules_order if module_status[n] == 'SUCCESS')
failed = total_modules - passed
total_time = sum(module_duration[n] for n in modules_order)
slowest = max(modules_order, key=lambda n: module_duration[n])
fastest = min(modules_order, key=lambda n: module_duration[n])

warn_sorted = sorted(warnings.items(), key=lambda x: (-x[1], x[0]))
err_sorted = sorted(errors.items(), key=lambda x: (-x[1], x[0]))
failed_modules = [n for n in modules_order if module_status[n] == 'FAILED']
total_warnings = sum(warnings.values())
total_errors = sum(errors.values())

out = []
out.append('=== ANDROID BUILD REPORT ===')
out.append('')
out.append('-- Module Summary --')
for n in modules_order:
    out.append('{}: {} ({}ms)'.format(n, module_status[n], module_duration[n]))
out.append('')
out.append('-- Build Statistics --')
out.append('Total modules: {}'.format(total_modules))
out.append('Passed: {}'.format(passed))
out.append('Failed: {}'.format(failed))
out.append('Total build time: {}ms'.format(total_time))
out.append('Slowest module: {} ({}ms)'.format(slowest, module_duration[slowest]))
out.append('Fastest module: {} ({}ms)'.format(fastest, module_duration[fastest]))
out.append('')
out.append('-- Warnings by Module --')
if warn_sorted:
    for n, c in warn_sorted:
        out.append('{}: {} warning(s)'.format(n, c))
else:
    out.append('(none)')
out.append('')
out.append('-- Errors by Module --')
if err_sorted:
    for n, c in err_sorted:
        out.append('{}: {} error(s)'.format(n, c))
else:
    out.append('(none)')
out.append('')
out.append('-- Action Items --')
if failed_modules:
    out.append('FAILED modules: {}'.format(', '.join(failed_modules)))
else:
    out.append('FAILED modules: none')
out.append('Total warnings: {}'.format(total_warnings))
out.append('Total errors: {}'.format(total_errors))

with open(report_path, 'w') as f:
    f.write('\n'.join(out) + '\n')

print('Done')
PYEOF
python3 /tmp/gen_report.py
cat /home/user/pipeline/build_report.txt
