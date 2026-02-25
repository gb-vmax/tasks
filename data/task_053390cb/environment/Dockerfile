FROM ubuntu:22.04

RUN <<'ENDPOST'
set -eux
    apt-get update
    apt-get install -y python3 python3-pip
    pip3 install --no-cache-dir pytest

    # Ensure /home/user/data exists with correct permissions
    mkdir -p /home/user/data
    chmod 755 /home/user
    chmod 755 /home/user/data

    # Create the resource_usage.csv file with required content and permissions
    cat > /home/user/data/resource_usage.csv <<EOF
department,server,cpu_usage
IT,server01,25.0
Marketing,server02,63.28
Sales,server03,41.2
Marketing,server08,62.21
IT,server09,24.8
Sales,server04,40.1
IT,server06,28.5
Marketing,server13,62.75
EOF
    chmod 644 /home/user/data/resource_usage.csv

    # Ensure the output JSON file does NOT exist
    rm -f /home/user/data/dept_with_highest_avg_cpu.json
ENDPOST

WORKDIR /home/user
