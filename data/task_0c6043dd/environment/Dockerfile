FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the data directory
mkdir -p /home/user/data

# Create the sales.csv file with the expected content
cat > /home/user/data/sales.csv << 'EOF'
date,category,product,units_sold,unit_price
2024-01-01,Electronics,Laptop,3,1200
2024-01-01,Furniture,Chair,10,85
2024-01-02,Electronics,Phone,7,650
2024-01-02,Clothing,Jacket,5,90
2024-01-03,Furniture,Desk,4,320
2024-01-03,Clothing,Shoes,12,60
2024-01-04,Electronics,Tablet,6,430
2024-01-04,Clothing,Hat,20,25
2024-01-05,Furniture,Lamp,8,45
2024-01-05,Electronics,Headphones,15,80
EOF

# Do NOT create category_revenue.txt — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
