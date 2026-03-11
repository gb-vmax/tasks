#!/bin/bash
set -e
cd /home/user

cat /home/user/workflows/process_orders.sh
cat /home/user/workflows/process_orders.sh
cat > /home/user/workflows/process_orders.sh << 'EOF'
#!/bin/bash

set -e

INPUT_DIR="/home/user/data/orders"
OUTPUT_DIR="/home/user/data/processed"

echo "Starting order processing workflow..."

TMPFILE=$(mktemp /tmp/orders_tmp.XXXXXX)
trap "rm -f $TMPFILE" EXIT INT TERM

# Aggregate orders from input directory
cat "$INPUT_DIR"/*.csv > $TMPFILE

# Filter out cancelled orders
grep -v "CANCELLED" $TMPFILE > "$OUTPUT_DIR/valid_orders.csv"

# Count processed orders
COUNT=$(wc -l < $TMPFILE)
echo "Processed $COUNT order lines."

# Clean up
rm -f $TMPFILE

echo "Workflow complete."
EOF
chmod +x /home/user/workflows/process_orders.sh && cat /home/user/workflows/process_orders.sh
ls -l /home/user/workflows/process_orders.sh && grep -c "orders_temp.csv" /home/user/workflows/process_orders.sh
