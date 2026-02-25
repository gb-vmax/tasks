FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install Python3 and pip
    apt-get update
    apt-get install -y python3 python3-pip

    # Install pytest
    pip3 install pytest

    # Create the user and home directory if not present (for consistency)
    if ! id user >/dev/null 2>&1; then
        useradd -m -s /bin/bash user
    fi

    # Create migration logs directory with user-writable permissions
    mkdir -p /home/user/migration/logs
    chown user:user /home/user/migration/logs
    chmod 700 /home/user/migration/logs

    # Create the deployments.log file with the exact required content
    cat > /home/user/migration/logs/deployments.log <<'EOF'
2024-06-05T10:01:22Z INFO: auth-service deploy started
2024-06-05T10:01:25Z ERROR: auth-service deploy failed
2024-06-05T10:02:10Z INFO: payment-service deploy started
2024-06-05T10:02:13Z ERROR: payment-service deploy failed
2024-06-05T10:03:40Z ERROR: malformed line deploy fail
2024-06-05T10:04:00Z ERROR: deploy failed
2024-06-05T10:04:22Z ERROR: inventory_service deploy failed
2024-06-05T10:05:05Z DEBUG: monitoring started
2024-06-05T10:07:11Z ERROR: deploy failed - timed out
EOF

    # Set ownership and permissions for the log file
    chown user:user /home/user/migration/logs/deployments.log
    chmod 600 /home/user/migration/logs/deployments.log

    # Ensure failed_services.log does NOT exist
    rm -f /home/user/migration/logs/failed_services.log
ENDPOST

WORKDIR /home/user
