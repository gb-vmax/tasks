#!/bin/bash
set -e
cd /home/user

cat /home/user/store/products.csv
python3 -c "
import csv, json

with open('/home/user/store/products.csv', newline='') as f:
    reader = csv.DictReader(f)
    active = []
    for row in reader:
        if row['status'] == 'active':
            active.append({
                'id': row['product_id'],
                'name': row['product_name'],
                'price': float(row['price']),
                'category': row['category']
            })

output = json.dumps(active, indent=2)
# Remove trailing newline if present
with open('/home/user/store/active_products.json', 'w') as f:
    f.write(output)
"
cat /home/user/store/active_products.json
