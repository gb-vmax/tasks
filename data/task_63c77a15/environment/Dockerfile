FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create data directory and sales.csv input file
mkdir -p /home/user/data

cat > /home/user/data/sales.csv << 'EOF'
region,product,revenue
North,Widget A,450.00
South,Widget B,320.50
North,Widget C,890.25
East,Widget A,215.75
South,Widget B,540.00
North,Widget D,125.50
East,Widget C,678.90
West,Widget A,310.00
South,Widget B,430.75
West,Widget C,560.35
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
