FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install python3, pip, and pytest
    apt-get update
    apt-get install -y python3 python3-pip
    pip3 install --no-cache-dir pytest

    # Create user and data directories
    mkdir -p /home/user/data
    chown -R 1000:1000 /home/user
    chmod 755 /home/user
    chmod 755 /home/user/data

    # Create the sales.csv file with the required contents
    cat > /home/user/data/sales.csv <<'EOF'
ID,Date,Customer,Amount
1001,2023-01-01,Smith,500
1002,2023-01-02,Williams,300
BADLINE_MISSING_COLUMN
1003,2023-01-03,"O'Reilly, Jr.",700
1004,2023-01-04,Evans,200
1005,2023-01-05,"Miller, Anna",missing_amount
1006,2023-01-06,Patel,800
1007,2023-01-07,Chen,600
BROKEN,"2023-01-08,Lee
,
EOF

    # Set permissions: readable by non-root user
    chmod 644 /home/user/data/sales.csv
ENDPOST

WORKDIR /home/user
