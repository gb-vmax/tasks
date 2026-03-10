#!/bin/bash
set -e
cd /home/user

head -20 /home/user/support/tickets.tsv
wc -l /home/user/support/tickets.tsv && tail -20 /home/user/support/tickets.tsv
python3 << 'EOF'
from collections import Counter

# Read data
rows = []
with open('/home/user/support/tickets.tsv') as f:
    header = f.readline()  # skip header
    for line in f:
        parts = line.rstrip('\n').split('\t')
        rows.append(parts)

# Helper: sort by count desc, then label asc
def sorted_counts(counter):
    return sorted(counter.items(), key=lambda x: (-x[1], x[0]))

# Count by column index
def count_col(idx):
    return Counter(r[idx] for r in rows)

cat_counts    = count_col(2)
tech_counts   = count_col(3)
status_counts = count_col(4)
err_counts    = count_col(5)
pri_counts    = count_col(6)

# Top 5 error codes (with ties at position 5)
def top5_with_ties(counter):
    sorted_items = sorted_counts(counter)
    # Find the count at position 4 (index 4, i.e., 5th item)
    if len(sorted_items) <= 5:
        return sorted_items
    cutoff_count = sorted_items[4][1]
    return [(k, v) for k, v in sorted_items if v >= cutoff_count]

lines = []
lines.append('=== IT SUPPORT TICKET SUMMARY ===')
lines.append('')
lines.append('--- Tickets by Category ---')
for label, count in sorted_counts(cat_counts):
    lines.append(f'{count} {label}')
lines.append('')
lines.append('--- Tickets by Technician ---')
for label, count in sorted_counts(tech_counts):
    lines.append(f'{count} {label}')
lines.append('')
lines.append('--- Tickets by Status ---')
for label, count in sorted_counts(status_counts):
    lines.append(f'{count} {label}')
lines.append('')
lines.append('--- Top Error Codes ---')
for label, count in top5_with_ties(err_counts):
    lines.append(f'{count} {label}')
lines.append('')
lines.append('--- Tickets by Priority ---')
for label, count in sorted_counts(pri_counts):
    lines.append(f'{count} {label}')

with open('/home/user/support/summary_report.txt', 'w') as f:
    f.write('\n'.join(lines) + '\n')

# Technician load file
with open('/home/user/support/technician_load.txt', 'w') as f:
    for label, count in sorted_counts(tech_counts):
        f.write(label + '\n')

print("Done!")
EOF
cat /home/user/support/summary_report.txt
cat /home/user/support/technician_load.txt
