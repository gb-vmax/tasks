#!/bin/bash
set -e
cd /home/user

cat /home/user/data/sales.csv
python3 -c "
import csv
from collections import defaultdict

with open('/home/user/data/sales.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

total_records = len(rows)
total_units = sum(int(r['units_sold']) for r in rows)
total_revenue = sum(int(r['revenue']) for r in rows)

region_revenue = defaultdict(int)
product_units = defaultdict(int)

for r in rows:
    region_revenue[r['region']] += int(r['revenue'])
    product_units[r['product']] += int(r['units_sold'])

sorted_regions = sorted(region_revenue.items(), key=lambda x: x[1], reverse=True)
top_product = max(product_units.items(), key=lambda x: x[1])

lines = []
lines.append('=== SALES DATA SUMMARY ===')
lines.append(f'Total records: {total_records}')
lines.append(f'Total units sold: {total_units}')
lines.append(f'Total revenue: {total_revenue}')
lines.append('')
lines.append('=== REVENUE BY REGION ===')
for region, rev in sorted_regions:
    lines.append(f'  {region}: {rev}')
lines.append('')
lines.append('=== TOP PRODUCT BY UNITS SOLD ===')
lines.append(f'  {top_product[0]}: {top_product[1]}')

with open('/home/user/data/sales_summary.txt', 'w') as f:
    f.write('\n'.join(lines) + '\n')
"
cat /home/user/data/sales_summary.txt
