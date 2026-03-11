FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the ETL directory structure
mkdir -p /home/user/etl/incoming

# Create customers.csv
cat > /home/user/etl/incoming/customers.csv << 'EOF'
id,name,email
1,Alice,alice@example.com
2,Bob,bob@example.com
3,Carol,carol@example.com
EOF

# Create orders.csv
cat > /home/user/etl/incoming/orders.csv << 'EOF'
order_id,customer_id,amount
101,1,59.99
102,2,120.00
103,1,34.50
EOF

# Create products.csv
cat > /home/user/etl/incoming/products.csv << 'EOF'
product_id,name,price
1001,Widget,9.99
1002,Gadget,24.99
1003,Doohickey,4.49
EOF

# Do NOT create checksums.sha256 — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
