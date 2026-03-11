#!/bin/bash
set -e
cd /home/user

cat /home/user/monitoring/uptime_report.json
cat > /tmp/gen_report.py << 'PYEOF'
import json

with open('/home/user/monitoring/uptime_report.json') as f:
    data = json.load(f)

services = data['services']
services_sorted = sorted(services, key=lambda s: s['name'])
checks_per_service = len(services[0]['checks'])

stats = []
for svc in services_sorted:
    name = svc['name']
    sla_target = svc['sla_target_pct']
    checks = svc['checks']
    total = len(checks)
    up_checks = [c for c in checks if c['status'] == 'up']
    down_checks = [c for c in checks if c['status'] == 'down']
    up_count = len(up_checks)
    down_count = len(down_checks)
    uptime_pct = round(up_count / total * 100, 2)
    sla_status = 'BREACH' if uptime_pct < sla_target else 'OK'
    avg_ms = round(sum(c['response_time_ms'] for c in up_checks) / up_count) if up_count > 0 else 0
    stats.append({'name': name, 'sla_target': sla_target, 'total': total, 'up_count': up_count, 'down_count': down_count, 'uptime_pct': uptime_pct, 'sla_status': sla_status, 'avg_ms': avg_ms})

total_services = len(stats)
total_checks = sum(s['total'] for s in stats)
total_up = sum(s['up_count'] for s in stats)
global_uptime = round(total_up / total_checks * 100, 2)
slowest = sorted(stats, key=lambda s: (-s['avg_ms'], s['name']))[0]
breaches = [s for s in stats if s['sla_status'] == 'BREACH']

lines = []
lines.append('=== SLA COMPLIANCE REPORT ===')
lines.append('Generated checks per service: {}'.format(checks_per_service))
lines.append('')
lines.append('SERVICE SUMMARY')
lines.append('---------------')

for i, s in enumerate(stats):
    lines.append(s['name'])
    lines.append('  Checks: {} | Up: {} | Down: {}'.format(s['total'], s['up_count'], s['down_count']))
    lines.append('  Uptime: {:.2f}%'.format(s['uptime_pct']))
    lines.append('  SLA Target: {}%'.format(s['sla_target']))
    lines.append('  SLA Status: {}'.format(s['sla_status']))
    lines.append('  Avg Response (up checks): {}ms'.format(s['avg_ms']))
    if i < len(stats) - 1:
        lines.append('')

lines.append('')
lines.append('=== BREACH SUMMARY ===')
lines.append('Services in breach: {}'.format(len(breaches)))
if breaches:
    for b in breaches:
        lines.append('{}: {:.2f}% uptime (target: {}%)'.format(b['name'], b['uptime_pct'], b['sla_target']))
else:
    lines.append('No SLA breaches detected.')

lines.append('')
lines.append('=== OVERALL STATS ===')
lines.append('Total services: {}'.format(total_services))
lines.append('Total checks: {}'.format(total_checks))
lines.append('Global uptime: {:.2f}%'.format(global_uptime))
lines.append('Slowest avg response: {} ({}ms)'.format(slowest['name'], slowest['avg_ms']))

with open('/home/user/monitoring/sla_report.txt', 'w') as out:
    out.write('\n'.join(lines) + '\n')
print('Done')
PYEOF
python3 /tmp/gen_report.py
cat /home/user/monitoring/sla_report.txt
