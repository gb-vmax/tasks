FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the data directory
mkdir -p /home/user/data

# Create the sales.csv file with the expected content
cat > /home/user/data/sales.csv << 'EOF'
region,category,month,units_sold,revenue
North,Electronics,January,120,8400
South,Clothing,January,45,2250
East,Electronics,January,98,6860
West,Clothing,January,30,1500
North,Furniture,February,15,7500
South,Electronics,February,80,5600
East,Clothing,February,55,2750
West,Electronics,February,110,7700
North,Clothing,March,60,3000
South,Furniture,March,12,4800
East,Furniture,March,18,9000
West,Furniture,March,9,3150
EOF

# Ensure correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
