FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install Python3, pip, and pytest
    apt-get update
    apt-get install -y python3 python3-pip
    pip3 install pytest

    # Create the user and home directory if not already present
    useradd -m user || true

    # Create the microservice_logs directory
    mkdir -p /home/user/microservice_logs
    chown user:user /home/user/microservice_logs
    chmod 755 /home/user/microservice_logs

    # Create api.log with specified contents
    cat > /home/user/microservice_logs/api.log <<EOF
2024-06-18 14:02:07 INFO Connected to API Gateway.
2024-06-18 14:03:01 ERROR Failed to fetch user data.
2024-06-18 14:03:45 WARN Response time high.
2024-06-18 14:04:00 ERROR Token expired.
EOF

    # Create db.log with specified contents
    cat > /home/user/microservice_logs/db.log <<EOF
2024-06-18 14:02:10 INFO Database connection established.
2024-06-18 14:03:05 ERROR Connection timeout.
2024-06-18 14:03:50 WARN Slow query detected.
EOF

    # Create cache.log with specified contents
    cat > /home/user/microservice_logs/cache.log <<EOF
2024-06-18 14:02:15 INFO Cache initialized.
2024-06-18 14:03:10 ERROR Redis unreachable.
2024-06-18 14:03:55 INFO Cache hit rate: 95%.
EOF

    # Set ownership and permissions
    chown user:user /home/user/microservice_logs/*.log
    chmod 644 /home/user/microservice_logs/*.log
ENDPOST

WORKDIR /home/user
