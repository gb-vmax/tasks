#!/bin/bash
set -e
cd /home/user

cat /home/user/audit/access_log.csv
python3 << 'EOF'
import csv

rows = []
with open('/home/user/audit/access_log.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['status'] == 'FAILURE':
            rows.append(row)

# Sort by username, then timestamp
rows.sort(key=lambda r: (r['username'], r['timestamp']))

def reformat_ts(ts):
    # YYYY-MM-DD HH:MM:SS -> DD/MM/YYYY HH:MM
    date_part, time_part = ts.split(' ')
    y, m, d = date_part.split('-')
    hh, mm, ss = time_part.split(':')
    return f"{d}/{m}/{y} {hh}:{mm}"

sep = '-' * 36
lines = []
lines.append("AUDIT TRAIL - FAILED LOGIN ATTEMPTS")
lines.append(sep)
for row in rows:
    ts = reformat_ts(row['timestamp'])
    lines.append(f"[{ts}] {row['username']} @ {row['source_ip']}")
lines.append(sep)
lines.append(f"Total failed attempts: {len(rows)}")

with open('/home/user/audit/trail_report.txt', 'w') as f:
    f.write('\n'.join(lines) + '\n')

print("Done")
EOF
cat /home/user/audit/trail_report.txt
