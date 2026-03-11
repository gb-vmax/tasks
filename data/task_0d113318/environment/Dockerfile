FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the workflows directory
mkdir -p /home/user/workflows
mkdir -p /home/user/data/orders
mkdir -p /home/user/data/processed

# Create the vulnerable script with hardcoded temp path
cat > /home/user/workflows/process_orders.sh << 'EOF'
#!/bin/bash

set -e

INPUT_DIR="/home/user/data/orders"
OUTPUT_DIR="/home/user/data/processed"

echo "Starting order processing workflow..."

/tmp/orders_temp.csv

# Aggregate orders from input directory
cat "$INPUT_DIR"/*.csv > /tmp/orders_temp.csv

# Filter out cancelled orders
grep -v "CANCELLED" /tmp/orders_temp.csv > "$OUTPUT_DIR/valid_orders.csv"

# Count processed orders
COUNT=$(wc -l < /tmp/orders_temp.csv)
echo "Processed $COUNT order lines."

# Clean up
rm -f /tmp/orders_temp.csv

echo "Workflow complete."
EOF

# Make the script executable
chmod +x /home/user/workflows/process_orders.sh

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
