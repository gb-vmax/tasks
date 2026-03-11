FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the data directory
mkdir -p /home/user/data

# Create the sales PSV file with header and 5 data records
cat > /home/user/data/sales.psv << 'EOF'
REGION|SALESPERSON|PRODUCT|UNITS|UNIT_PRICE
West|Alice|Widget|12|4.50
East|Bob|Gadget|7|15.00
North|Carol|Widget|3|4.50
South|Dave|Doohickey|20|8.75
East|Alice|Gadget|5|15.00
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
