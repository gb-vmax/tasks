FROM ubuntu:22.04

RUN <<'ENDPOST'
set -eux

    # Create user and home directory if not present
    useradd -m user || true

    # Ensure /home/user exists and is owned by user
    mkdir -p /home/user
    chown user:user /home/user

    # Create the input CSV file with specified contents
    cat > /home/user/audit_runs.csv <<'EOF'
run_id,pipeline,developer,start_time,status,duration_seconds
1001,deploy-api,alice,2024-05-20T08:15:00Z,success,130
1002,deploy-web,bob,2024-05-20T08:17:23Z,fail,95
1003,deploy-api,charlie,2024-05-20T09:01:11Z,success,110
EOF

    # Set correct permissions for the CSV and its directory
    chown user:user /home/user/audit_runs.csv
    chmod 644 /home/user/audit_runs.csv

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest
ENDPOST

WORKDIR /home/user
