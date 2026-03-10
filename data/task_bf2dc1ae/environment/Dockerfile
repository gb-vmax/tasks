FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the ETL schemas directory
mkdir -p /home/user/etl/schemas

# Create the schema CSV file
cat > /home/user/etl/schemas/orders_pipeline.csv << 'EOF'
field_name,data_type,nullable,description
order_id,INTEGER,NO,Unique identifier for the order
customer_id,INTEGER,NO,Foreign key to the customers table
order_date,TIMESTAMP,NO,Date and time the order was placed
status,STRING,NO,Current status of the order
total_amount,FLOAT,YES,Total monetary value of the order
discount_code,STRING,YES,Promotional discount code applied
EOF

# Do NOT create the docs directory or any output files
# The agent will create those as part of the task

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
