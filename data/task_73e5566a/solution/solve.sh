#!/bin/bash
set -e
cd /home/user

cat /home/user/data/training_samples.csv
python3 -c "
import csv

filepath = '/home/user/data/training_samples.csv'

with open(filepath, newline='') as f:
    reader = csv.reader(f)
    headers = next(reader)
    rows = list(reader)

total_rows = len(rows)
total_cols = len(headers)

col_stats = []
for i, col in enumerate(headers):
    values = [row[i] for row in rows]
    missing = sum(1 for v in values if v.strip() == '')
    numeric = []
    for v in values:
        v = v.strip()
        if v != '':
            try:
                numeric.append(float(v))
            except ValueError:
                pass
    if numeric:
        min_str = str(int(min(numeric)))
        max_str = str(int(max(numeric)))
    else:
        min_str = 'N/A'
        max_str = 'N/A'
    col_stats.append((col, min_str, max_str, missing))

total_missing = sum(s[3] for s in col_stats)
cols_with_missing = sum(1 for s in col_stats if s[3] > 0)

lines = []
lines.append('=== DATASET DIAGNOSTIC REPORT ===')
lines.append('')
lines.append('File: /home/user/data/training_samples.csv')
lines.append('Total rows (excluding header): ' + str(total_rows))
lines.append('Total columns: ' + str(total_cols))
lines.append('')
lines.append('=== COLUMN STATS ===')
for col, mn, mx, miss in col_stats:
    lines.append(col + ': min=' + mn + ', max=' + mx + ', missing=' + str(miss))
lines.append('')
lines.append('=== MISSING VALUE SUMMARY ===')
lines.append('Total missing values: ' + str(total_missing))
lines.append('Columns with missing data: ' + str(cols_with_missing))

with open('/home/user/data/dataset_report.txt', 'w') as f:
    f.write('\n'.join(lines) + '\n')

print('Done')
"
cat /home/user/data/dataset_report.txt
