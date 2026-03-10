#!/bin/bash
set -e
cd /home/user

cat /home/user/capacity/server_metrics.csv | head -20
wc -l /home/user/capacity/server_metrics.csv && tail -20 /home/user/capacity/server_metrics.csv
python3 << 'EOF'
import csv
from datetime import datetime
import pytz

utc = pytz.utc
ny = pytz.timezone('America/New_York')

rows = []
with open('/home/user/capacity/server_metrics.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ts_utc = utc.localize(datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S'))
        ts_ny = ts_utc.astimezone(ny)
        rows.append({
            'ts_utc': ts_utc,
            'ts_ny': ts_ny,
            'cpu': float(row['cpu_percent']),
            'mem': float(row['mem_percent']),
        })

# Print converted times for verification
for r in rows:
    tz_name = r['ts_ny'].strftime('%Z')
    print(f"{r['ts_utc'].strftime('%Y-%m-%d %H:%M')} UTC -> {r['ts_ny'].strftime('%Y-%m-%d %H:%M')} {tz_name}  cpu={r['cpu']}  mem={r['mem']}")

EOF
python3 << 'EOF'
import csv
from datetime import datetime, timezone, timedelta
import zoneinfo

utc = timezone.utc
ny = zoneinfo.ZoneInfo('America/New_York')

rows = []
with open('/home/user/capacity/server_metrics.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ts_utc = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=utc)
        ts_ny = ts_utc.astimezone(ny)
        rows.append({
            'ts_utc': ts_utc,
            'ts_ny': ts_ny,
            'cpu': float(row['cpu_percent']),
            'mem': float(row['mem_percent']),
        })

for r in rows:
    tz_name = r['ts_ny'].strftime('%Z')
    print(f"{r['ts_utc'].strftime('%Y-%m-%d %H:%M')} UTC -> {r['ts_ny'].strftime('%Y-%m-%d %H:%M')} {tz_name}  cpu={r['cpu']}  mem={r['mem']}")
EOF
ls /usr/share/zoneinfo/America/ | grep -i new
find / -name "New_York" 2>/dev/null | head -10
python3 -c "
import csv
from datetime import datetime, timedelta

# DST transition for America/New_York in 2024:
# Clocks spring forward on March 10, 2024 at 2:00 AM EST = 7:00 AM UTC
# Before 2024-03-10 07:00:00 UTC: EST (UTC-5)
# From  2024-03-10 07:00:00 UTC: EDT (UTC-4)

dst_start_utc = datetime(2024, 3, 10, 7, 0, 0)

rows = []
with open('/home/user/capacity/server_metrics.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ts_utc = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S')
        if ts_utc < dst_start_utc:
            offset = timedelta(hours=-5)
            tz_name = 'EST'
        else:
            offset = timedelta(hours=-4)
            tz_name = 'EDT'
        ts_ny = ts_utc + offset
        rows.append({
            'ts_utc': ts_utc,
            'ts_ny': ts_ny,
            'tz_name': tz_name,
            'cpu': float(row['cpu_percent']),
            'mem': float(row['mem_percent']),
        })

for r in rows:
    print(f\"{r['ts_utc'].strftime('%Y-%m-%d %H:%M')} UTC -> {r['ts_ny'].strftime('%Y-%m-%d %H:%M')} {r['tz_name']}  cpu={r['cpu']}  mem={r['mem']}\")
"
python3 -c "
import csv
from datetime import datetime, timedelta
from collections import defaultdict

dst_start_utc = datetime(2024, 3, 10, 7, 0, 0)

rows = []
with open('/home/user/capacity/server_metrics.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ts_utc = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S')
        if ts_utc < dst_start_utc:
            offset = timedelta(hours=-5)
            tz_name = 'EST'
        else:
            offset = timedelta(hours=-4)
            tz_name = 'EDT'
        ts_ny = ts_utc + offset
        rows.append({'ts_utc': ts_utc, 'ts_ny': ts_ny, 'tz_name': tz_name,
                     'cpu': float(row['cpu_percent']), 'mem': float(row['mem_percent'])})

# Overall averages
avg_cpu = round(sum(r['cpu'] for r in rows) / len(rows), 2)
avg_mem = round(sum(r['mem'] for r in rows) / len(rows), 2)

# Hourly grouping by (date, hour, tz_name)
cpu_hours = defaultdict(list)
mem_hours = defaultdict(list)
for r in rows:
    key = (r['ts_ny'].strftime('%Y-%m-%d'), r['ts_ny'].hour, r['tz_name'])
    cpu_hours[key].append(r['cpu'])
    mem_hours[key].append(r['mem'])

best_cpu_key = max(cpu_hours, key=lambda k: sum(cpu_hours[k])/len(cpu_hours[k]))
best_mem_key = max(mem_hours, key=lambda k: sum(mem_hours[k])/len(mem_hours[k]))

peak_cpu = '{} {:02d}:00 {}'.format(best_cpu_key[0], best_cpu_key[1], best_cpu_key[2])
peak_mem = '{} {:02d}:00 {}'.format(best_mem_key[0], best_mem_key[1], best_mem_key[2])

# DST transition row
first_edt = next(r for r in rows if r['tz_name'] == 'EDT')
first_edt_str = first_edt['ts_ny'].strftime('%Y-%m-%d %H:%M') + ' EDT'

# High intervals
high_cpu = sum(1 for r in rows if r['cpu'] > 75.0)
high_mem = sum(1 for r in rows if r['mem'] > 80.0)

print('avg_cpu:', avg_cpu)
print('avg_mem:', avg_mem)
print('peak_cpu:', peak_cpu)
print('peak_mem:', peak_mem)
print('first_edt:', first_edt_str)
print('high_cpu:', high_cpu)
print('high_mem:', high_mem)
"
cat > /home/user/capacity/usage_report.txt << 'EOF'
=== SERVER CAPACITY REPORT ===
Server: srv-01
Report timezone: America/New_York

--- CPU ANALYSIS ---
Overall average CPU: 52.34%
Peak CPU hour: 2024-03-10 00:00 EST
High CPU intervals (>75%): 4

--- MEMORY ANALYSIS ---
Overall average memory: 68.84%
Peak memory hour: 2024-03-10 01:00 EST
High memory intervals (>80%): 4

--- DST NOTE ---
First EDT interval: 2024-03-10 03:00 EDT
EOF
cat /home/user/capacity/usage_report.txt
cat -A /home/user/capacity/usage_report.txt
