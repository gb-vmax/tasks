#!/bin/bash
set -e
cd /home/user

cat /home/user/ml_project/raw_samples.csv
python3 << 'EOF'
import csv
import sys

input_path = '/home/user/ml_project/raw_samples.csv'
clean_path = '/home/user/ml_project/clean_samples.csv'
rejected_path = '/home/user/ml_project/rejected_samples.csv'

clean_rows = []
rejected_rows = []

with open(input_path, 'r', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        # Check missing fields
        if len(row) < 4 or any(field.strip() == '' for field in row[:4]):
            rejected_rows.append(row + ['missing_field'])
            continue
        
        sample_id, feature1_str, feature2_str, label_str = row[0], row[1], row[2], row[3]
        
        # Check feature1
        try:
            f1 = float(feature1_str)
            if f1 < -10.0 or f1 > 10.0:
                raise ValueError
        except ValueError:
            rejected_rows.append(row + ['invalid_feature1'])
            continue
        
        # Check feature2
        try:
            f2 = float(feature2_str)
            if f2 < -10.0 or f2 > 10.0:
                raise ValueError
        except ValueError:
            rejected_rows.append(row + ['invalid_feature2'])
            continue
        
        # Check label
        try:
            lbl = int(label_str)
            if lbl not in (0, 1):
                raise ValueError
        except ValueError:
            rejected_rows.append(row + ['invalid_label'])
            continue
        
        clean_rows.append(row)

# Write clean file (no trailing newline)
with open(clean_path, 'w', newline='') as f:
    lines = [','.join(header)]
    for row in clean_rows:
        lines.append(','.join(row))
    f.write('\n'.join(lines))

# Write rejected file (no trailing newline)
rejected_header = header + ['error_reason']
with open(rejected_path, 'w', newline='') as f:
    lines = [','.join(rejected_header)]
    for row in rejected_rows:
        lines.append(','.join(row))
    f.write('\n'.join(lines))

print("Done.")
print(f"Clean rows: {len(clean_rows)}")
print(f"Rejected rows: {len(rejected_rows)}")
EOF
echo "=== clean_samples.csv ===" && cat /home/user/ml_project/clean_samples.csv && echo "" && echo "=== rejected_samples.csv ===" && cat /home/user/ml_project/rejected_samples.csv
xxd /home/user/ml_project/clean_samples.csv | tail -3 && echo "---" && xxd /home/user/ml_project/rejected_samples.csv | tail -3
od -c /home/user/ml_project/clean_samples.csv | tail -3 && echo "---" && od -c /home/user/ml_project/rejected_samples.csv | tail -3
