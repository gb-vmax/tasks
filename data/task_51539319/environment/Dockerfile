FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create data directory
mkdir -p /home/user/data

# Create the sales CSV file
cat > /home/user/data/sales.csv << 'EOF'
transaction_id,date,salesperson,region,product,quantity,unit_price,total
1001,2024-01-15,Alice,North,Widget,10,5.99,59.90
1002,2024-01-16,Bob,South,Gadget,3,24.99,74.97
1003,2024-01-17,Alice,North,Widget,7,5.99,41.93
1004,2024-01-18,Carol,East,Doohickey,2,49.99,99.98
1005,2024-01-19,Bob,South,Widget,15,5.99,89.85
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
