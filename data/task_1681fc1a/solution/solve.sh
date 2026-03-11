#!/bin/bash
set -e
cd /home/user

cat /home/user/data/sales.csv
python3 -c "
import csv

input_file = '/home/user/data/sales.csv'
clean_file = '/home/user/data/sales_clean.csv'
summary_file = '/home/user/data/sales_summary.txt'

valid_regions = {'north', 'south', 'east', 'west'}

valid_rows = []
revenue = {'north': 0.0, 'south': 0.0, 'east': 0.0, 'west': 0.0}

with open(input_file, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    valid_rows.append(header)
    for row in reader:
        if len(row) != 5:
            continue
        tid, product, quantity, unit_price, region = row
        # Check quantity is positive integer
        try:
            q = int(quantity)
            if q <= 0:
                continue
        except ValueError:
            continue
        # Check unit_price is positive number
        try:
            p = float(unit_price)
            if p <= 0:
                continue
        except ValueError:
            continue
        # Check region
        if region not in valid_regions:
            continue
        valid_rows.append(row)
        revenue[region] += q * p

with open(clean_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(valid_rows)

grand_total = sum(revenue.values())

with open(summary_file, 'w') as f:
    f.write('Sales Summary\n')
    f.write('=============\n')
    f.write('\n')
    for region in sorted(valid_regions):
        f.write(f'{region}: {revenue[region]:.2f}\n')
    f.write(f'Total: {grand_total:.2f}')
"
cat /home/user/data/sales_clean.csv
cat /home/user/data/sales_summary.txt
