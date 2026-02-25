FROM ubuntu:22.04

ENV SESSION_OWNER="alice.smith"
ENV SESSION_ID="stag-20230501-001"

RUN <<'ENDPOST'
set -eux

    # Create user and home directory if not already present
    if ! id -u user >/dev/null 2>&1; then
        useradd -m -s /bin/bash user
    fi

    # Ensure pip and python3 are installed for pytest
    apt-get update
    apt-get install -y python3 python3-pip

    pip3 install --no-cache-dir pytest

    # Create .dashboard_tune directory in home
    install -o user -g user -d /home/user/.dashboard_tune

    # Create dashboard.env with the required content
    cat > /home/user/.dashboard_tune/dashboard.env <<EOF
DASHBOARD_TITLE=Staging Observability
DEBUG_MODE=true
LOG_LEVEL=info
DATASOURCE_URL=https://logs-staging.example.com/query
REFRESH_INTERVAL=30
EOF

    # Set permissions: user-writable files and dir
    chown user:user /home/user/.dashboard_tune /home/user/.dashboard_tune/dashboard.env
    chmod 700 /home/user/.dashboard_tune
    chmod 600 /home/user/.dashboard_tune/dashboard.env

    # Create merged log file with correct content and order
    cat > /home/user/.dashboard_tune/settings_merged.log <<EOF
DASHBOARD_TITLE=Staging Observability
DEBUG_MODE=true
LOG_LEVEL=info
DATASOURCE_URL=https://logs-staging.example.com/query
REFRESH_INTERVAL=30
SESSION_OWNER=alice.smith
SESSION_ID=stag-20230501-001
EOF

    chown user:user /home/user/.dashboard_tune/settings_merged.log
    chmod 600 /home/user/.dashboard_tune/settings_merged.log
ENDPOST

WORKDIR /home/user
