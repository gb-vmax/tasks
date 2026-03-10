FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the store directory
mkdir -p /home/user/store

# Create the products CSV file
cat > /home/user/store/products.csv << 'EOF'
product_id,product_name,price,category,status
P001,Widget A,9.99,widgets,active
P002,Gadget Pro,24.50,gadgets,inactive
P003,Thingamajig,4.75,misc,active
P004,Super Widget,14.99,widgets,inactive
P005,Doohickey,7.25,misc,active
P006,Mega Gadget,49.99,gadgets,active
EOF

# Do NOT create active_products.json — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
