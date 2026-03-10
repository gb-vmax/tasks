FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create source data directories
mkdir -p /home/user/data/quarterly
mkdir -p /home/user/data/customers

# Create q1 sales data file
cat > /home/user/data/quarterly/q1_sales_data.csv << 'EOF'
date,region,amount
2024-01-15,north,1500.00
2024-02-20,south,2300.50
EOF

# Create q2 sales data file
cat > /home/user/data/quarterly/q2_sales_data.csv << 'EOF'
date,region,amount
2024-04-10,east,980.00
2024-05-18,west,4100.75
EOF

# Create master customers file
cat > /home/user/data/customers/master_customers.csv << 'EOF'
id,name,email
1,Alice,alice@example.com
2,Bob,bob@example.com
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
