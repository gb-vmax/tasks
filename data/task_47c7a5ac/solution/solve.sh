#!/bin/bash
set -e
cd /home/user

head -20 /home/user/storage/file_audit.log
wc -l /home/user/storage/file_audit.log && cat /home/user/storage/file_audit.log
python3 << 'EOF'
from collections import defaultdict
import os

log_file = '/home/user/storage/file_audit.log'
user_counts = defaultdict(int)
ext_counts = defaultdict(int)

with open(log_file, 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        parts = line.split('\t')
        if len(parts) != 3:
            continue
        size, username, filepath = parts
        user_counts[username] += 1
        filename = os.path.basename(filepath)
        if '.' in filename:
            ext = filename.rsplit('.', 1)[1]
        else:
            ext = '(none)'
        ext_counts[ext] += 1

# Sort users: by count desc, then alpha
sorted_users = sorted(user_counts.items(), key=lambda x: (-x[1], x[0]))
# Sort extensions: by count desc, then alpha
sorted_exts = sorted(ext_counts.items(), key=lambda x: (-x[1], x[0]))

total_files = sum(user_counts.values())
total_users = len(user_counts)
total_exts = len(ext_counts)

top3_users = sorted_users[:3]
top5_exts = sorted_exts[:5]

report_lines = []
report_lines.append('=== DISK USAGE REPORT ===')
report_lines.append('')
report_lines.append('-- Top 3 Users by File Count --')
for i, (user, count) in enumerate(top3_users, 1):
    report_lines.append(f'{i}. {user}: {count} files')
report_lines.append('')
report_lines.append('-- Top 5 Extensions by File Count --')
for i, (ext, count) in enumerate(top5_exts, 1):
    report_lines.append(f'{i}. {ext}: {count} files')
report_lines.append('')
report_lines.append('-- Summary --')
report_lines.append(f'Total files: {total_files}')
report_lines.append(f'Total unique users: {total_users}')
report_lines.append(f'Total unique extensions: {total_exts}')

output = '\n'.join(report_lines) + '\n'

with open('/home/user/storage/disk_report.txt', 'w') as f:
    f.write(output)

print("Report written successfully.")
print(output)
EOF
cat /home/user/storage/disk_report.txt
