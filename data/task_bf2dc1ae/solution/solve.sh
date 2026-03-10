#!/bin/bash
set -e
cd /home/user

cat /home/user/etl/schemas/orders_pipeline.csv
mkdir -p /home/user/etl/docs
cat > /home/user/etl/docs/orders_pipeline.md << 'EOF'
# orders Pipeline Documentation

## Overview

Pipeline: orders  
Source: PostgreSQL  
Destination: BigQuery  
Owner: data-eng-team  

## Schema

| Field Name | Data Type | Nullable | Description |
|---|---|---|---|
| order_id | INTEGER | NO | Unique identifier for the order |
| customer_id | INTEGER | NO | Foreign key to the customers table |
| order_date | TIMESTAMP | NO | Date and time the order was placed |
| status | STRING | NO | Current status of the order |
| total_amount | FLOAT | YES | Total monetary value of the order |
| discount_code | STRING | YES | Promotional discount code applied |

## Notes

- Schema version: 1.0
- Last updated: 2024-01-15
- Do not modify this file manually; it is generated from the schema CSV.
EOF
grep -c '^|' /home/user/etl/docs/orders_pipeline.md | awk '{print $1 - 2}' > /home/user/etl/docs/row_count.txt && cat /home/user/etl/docs/row_count.txt
python3 -c "
lines = [l.rstrip('\n') for l in open('/home/user/etl/docs/orders_pipeline.md') if l.startswith('|')]
total = len(lines)
malformed = [l for l in lines if not l.endswith('|')]
if malformed:
    result = 'LINT FAILED: malformed table lines found'
else:
    result = f'LINT PASSED: all {total} table lines are properly closed'
open('/home/user/etl/docs/lint_result.txt', 'w').write(result + '\n')
print(result)
"
echo "=== orders_pipeline.md ===" && cat /home/user/etl/docs/orders_pipeline.md && echo "=== row_count.txt ===" && cat /home/user/etl/docs/row_count.txt && echo "=== lint_result.txt ===" && cat /home/user/etl/docs/lint_result.txt
