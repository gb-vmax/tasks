#!/bin/bash
set -e
cd /home/user

ls /home/user/iot_logs/
cat /home/user/iot_logs/zone_factory.log
cat /home/user/iot_logs/zone_warehouse.log
cat /home/user/iot_logs/zone_outdoor.log
python3 -c "
from collections import Counter

zones = ['factory', 'warehouse', 'outdoor']
files = {'factory': '/home/user/iot_logs/zone_factory.log', 'warehouse': '/home/user/iot_logs/zone_warehouse.log', 'outdoor': '/home/user/iot_logs/zone_outdoor.log'}

zone_data = {}
for zone in zones:
    with open(files[zone]) as f:
        events = [line.strip() for line in f if line.strip()]
    counter = Counter(events)
    total = sum(counter.values())
    distinct = len(counter)
    top3 = sorted(counter.items(), key=lambda x: (-x[1], x[0]))[:3]
    zone_data[zone] = {'counter': counter, 'total': total, 'distinct': distinct, 'top3': top3}

all_codes = set(zone_data['factory']['counter'].keys())
for zone in zones[1:]:
    all_codes &= set(zone_data[zone]['counter'].keys())
cross = ','.join(sorted(all_codes)) if all_codes else 'NONE'
grand_total = sum(zone_data[z]['total'] for z in zones)

lines = ['=== IoT Telemetry Frequency Report ===']
for zone in zones:
    d = zone_data[zone]
    lines.append('')
    lines.append('[ZONE: {}]'.format(zone))
    lines.append('Total events: {}'.format(d['total']))
    lines.append('Distinct codes: {}'.format(d['distinct']))
    lines.append('Top 3:')
    for i, (code, cnt) in enumerate(d['top3'], 1):
        lines.append('  {}. {} ({})'.format(i, code, cnt))

lines.append('')
lines.append('[CROSS-ZONE]')
lines.append('Codes present in all 3 zones: {}'.format(cross))
lines.append('Grand total events: {}'.format(grand_total))

with open('/home/user/iot_logs/telemetry_report.txt', 'w') as f:
    f.write('\n'.join(lines))
print('Done')
"
cat /home/user/iot_logs/telemetry_report.txt
