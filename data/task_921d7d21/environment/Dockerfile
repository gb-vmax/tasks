FROM ubuntu:22.04

RUN <<'ENDPOST'
apt-get update
    apt-get install -y python3-pip
    pip3 install pytest

    # Create user if not present, with home directory
    if ! id user >/dev/null 2>&1; then
        useradd -m -s /bin/bash user
    fi

    # Ensure alerts directory exists and owned by user
    mkdir -p /home/user/alerts
    chown user:user /home/user/alerts

    # Create service_alerts.conf with exact contents and ownership
    cat > /home/user/alerts/service_alerts.conf <<EOF
THRESHOLD=85
NOTIFY_EMAIL=on
LOGFILE=/home/user/alerts/alert.log
ENABLED=true
EOF
    chown user:user /home/user/alerts/service_alerts.conf
    chmod 600 /home/user/alerts/service_alerts.conf

    # Create alert.log with the required line, ownership and permissions
    echo "[2024-06-11 12:00:00] ALERT: THRESHOLD exceeded (value: 92)" > /home/user/alerts/alert.log
    chown user:user /home/user/alerts/alert.log
    chmod 600 /home/user/alerts/alert.log
ENDPOST

WORKDIR /home/user
