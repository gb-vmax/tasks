FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest

    # Create the directory structure
    mkdir -p /home/user/services/payment-service

    # Create the initial payment.log file with the specified contents
    cat > /home/user/services/payment-service/payment.log <<EOF
[2024-06-13 09:04:01] [INFO] [init] Payment service starting
[2024-06-13 09:04:02] [ERROR] [transactions] Failed to process payment
[2024-06-13 09:04:03] [WARN] [db] Connection slow
[2024-06-13 09:04:04] [ERROR] [transactions] Invalid payment method
[2024-06-13 09:04:05] [ERROR] [api] Unexpected status code
[2024-06-13 09:04:06] [INFO] [monitor] Health check OK
EOF

    # Set permissions so that the user can read/write in the relevant directories and files
    chown -R 1000:1000 /home/user/services
    chmod -R u+rwX /home/user/services
ENDPOST

WORKDIR /home/user
