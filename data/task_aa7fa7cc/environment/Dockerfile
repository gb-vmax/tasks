FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e
    apt-get update
    apt-get install -y python3-pip
    pip3 install pytest

    # Create user and home directory if not present
    useradd -m user || true

    # Create /home/user/data directory
    mkdir -p /home/user/data
    chown user:user /home/user/data

    # Create /home/user/data/sales_data.csv with required content
    cat > /home/user/data/sales_data.csv <<EOF
Product,Date,Amount
Widget A,2023-06-01,120
Widget B,2023-06-02,130
Widget C,2023-06-03,150
Widget A,2023-06-04,100
EOF

    chown user:user /home/user/data/sales_data.csv
    chmod 644 /home/user/data/sales_data.csv
ENDPOST

WORKDIR /home/user
