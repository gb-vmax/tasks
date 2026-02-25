FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Create user and home directory if not present
    if ! id user 2>/dev/null; then
        useradd -m -s /bin/bash user
    fi

    # Ensure /home/user/etl_legacy exists
    mkdir -p /home/user/etl_legacy
    chown user:user /home/user/etl_legacy

    # Create sales_raw.csv with specified content
    cat > /home/user/etl_legacy/sales_raw.csv <<'EOF'
product,amount,date
Widget,100,2023-01-05
Gadget,150,2023-01-06
EOF

    # Create run_etl.py with specified content
    cat > /home/user/etl_legacy/run_etl.py <<'EOF'
import csv

with open('sales_raw.csv', newline='') as infile, open('sales_processed.csv', 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames + ['processed'])
    writer.writeheader()
    for row in reader:
        row['processed'] = 'yes'
        writer.writerow(row)
EOF

    # Set ownership and permissions for files and directory
    chown user:user /home/user/etl_legacy/sales_raw.csv /home/user/etl_legacy/run_etl.py
    chmod 755 /home/user/etl_legacy
    chmod 644 /home/user/etl_legacy/sales_raw.csv /home/user/etl_legacy/run_etl.py

    # Install Python3, pip, and pytest
    apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip
    pip3 install --no-cache-dir pytest
ENDPOST

WORKDIR /home/user
