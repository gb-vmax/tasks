FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the data directory
mkdir -p /home/user/data

# Create the sales CSV file
cat > /home/user/data/sales.csv << 'EOF'
date,region,product,units_sold,revenue
2024-01-01,North,Widget,50,2500
2024-01-01,South,Gadget,30,1800
2024-01-02,East,Widget,20,1000
2024-01-02,North,Gadget,40,2400
2024-01-03,South,Widget,60,3000
2024-01-03,West,Gizmo,25,1250
2024-01-04,East,Gizmo,35,1750
2024-01-04,West,Gadget,45,2700
2024-01-05,North,Gizmo,55,2750
2024-01-05,South,Widget,70,3500
EOF

# Do NOT create sales_summary.txt — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
