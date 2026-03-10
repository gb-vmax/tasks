#!/bin/bash
set -e
cd /home/user

head -20 /home/user/ml_data/raw_samples.csv
cat /home/user/ml_data/raw_samples.csv
python3 -c "
import csv

input_file = '/home/user/ml_data/raw_samples.csv'
output_file = '/home/user/ml_data/training_ready.csv'

rows = []
with open(input_file, 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if float(row['quality_score']) >= 0.75 and row['label'] != 'unknown':
            rows.append({
                'sample_id': int(row['sample_id']),
                'feature_a': row['feature_a'],
                'feature_b': row['feature_b'],
                'label': row['label']
            })

rows.sort(key=lambda x: x['sample_id'])

with open(output_file, 'w', newline='') as f:
    f.write('sample_id,feature_a,feature_b,label\n')
    for row in rows:
        f.write(f\"{row['sample_id']},{row['feature_a']},{row['feature_b']},{row['label']}\n\")

print('Done')
"
cat /home/user/ml_data/training_ready.csv
xxd /home/user/ml_data/training_ready.csv | tail -3
od -c /home/user/ml_data/training_ready.csv | tail -3
