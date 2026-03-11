#!/bin/bash
set -e
cd /home/user

cat /home/user/ml_project/training_data.csv
python3 -c "
import csv
from collections import defaultdict

data = defaultdict(list)

with open('/home/user/ml_project/training_data.csv') as f:
    reader = csv.reader(f)
    total = 0
    for row in reader:
        sample_id, f1, f2, label = row[0], float(row[1]), float(row[2]), row[3].strip()
        data[label].append((f1, f2))
        total += 1

lines = ['=== CLASS DISTRIBUTION REPORT ===', '']

for label in sorted(data.keys()):
    samples = data[label]
    count = len(samples)
    pct = count / total * 100
    f1_vals = [s[0] for s in samples]
    f2_vals = [s[1] for s in samples]
    line = f'{label}: {count} samples ({pct:.2f}%), feature1 range [{min(f1_vals):.2f}, {max(f1_vals):.2f}], feature2 range [{min(f2_vals):.2f}, {max(f2_vals):.2f}]'
    lines.append(line)

lines.append('')
lines.append(f'Total samples: {total}')

with open('/home/user/ml_project/class_stats.txt', 'w') as f:
    f.write('\n'.join(lines) + '\n')

print('Done')
"
cat /home/user/ml_project/class_stats.txt
