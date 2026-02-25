#!/bin/bash
set -e
cd /home/user

python3 -c "
import csv, json
with open('/home/user/audit_runs.csv') as f, open('/home/user/audit_runs.jsonl', 'w') as out:
    reader = csv.DictReader(f)
    for row in reader:
        row['run_id'] = int(row['run_id'])
        row['duration_seconds'] = int(row['duration_seconds'])
        json.dump(row, out)
        out.write('\n')
"
python3 -c "
import csv
from collections import defaultdict
data = defaultdict(list)
with open('/home/user/audit_runs.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data[row['pipeline']].append(row)
with open('/home/user/audit_summary.csv', 'w', newline='') as out:
    writer = csv.writer(out)
    writer.writerow(['pipeline','total_runs','success_count','fail_count','average_duration'])
    for pipeline in sorted(data):
        runs = data[pipeline]
        total_runs = len(runs)
        success_count = sum(1 for r in runs if r['status']=='success')
        fail_count = sum(1 for r in runs if r['status']=='fail')
        avg_duration = sum(int(r['duration_seconds']) for r in runs) // total_runs
        writer.writerow([pipeline, total_runs, success_count, fail_count, avg_duration])
"
echo -e "JSONL generated: /home/user/audit_runs.jsonl\nSummary CSV generated: /home/user/audit_summary.csv" > /home/user/audit_task.log
cat /home/user/audit_task.log
