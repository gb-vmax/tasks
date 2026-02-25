FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install Python3, pip, and pytest
    apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip
    pip3 install --no-cache-dir pytest

    # Create user and home directory if not already present
    if ! id user >/dev/null 2>&1; then
        useradd -m -d /home/user user
    fi
    mkdir -p /home/user

    # Create required directories
    mkdir -p /home/user/logs
    mkdir -p /home/user/scripts
    mkdir -p /home/user/errors

    # Set permissions to allow user-level read/write
    chmod 755 /home/user
    chmod 755 /home/user/logs
    chmod 755 /home/user/scripts
    chmod 755 /home/user/errors
    chown -R root:root /home/user

    # Populate log files with specified content
    cat > /home/user/logs/app_backend.log <<EOF
INFO Starting backend service
ERROR Database connection failed
INFO Retrying connection
ERROR Timeout occurred
WARNING Low available memory
ERROR Failed to handle request
EOF

    cat > /home/user/logs/app_frontend.log <<EOF
INFO User login attempt
WARNING Session expired
INFO Page rendered successfully
EOF

    cat > /home/user/logs/app_worker.log <<EOF
ERROR Task execution error: OutOfMemory
INFO Worker idle
WARNING High CPU usage
ERROR Unexpected shutdown
EOF

    cat > /home/user/logs/app_scheduler.log <<EOF
INFO Scheduler started
ERROR Failed to load schedule configuration
ERROR Invalid cron pattern detected
WARNING Next run delayed
EOF

    # Set permissions for log files
    chmod 644 /home/user/logs/app_backend.log
    chmod 644 /home/user/logs/app_frontend.log
    chmod 644 /home/user/logs/app_worker.log
    chmod 644 /home/user/logs/app_scheduler.log
    chown root:root /home/user/logs/app_backend.log
    chown root:root /home/user/logs/app_frontend.log
    chown root:root /home/user/logs/app_worker.log
    chown root:root /home/user/logs/app_scheduler.log

    # Ensure scripts directory is writable and empty (no extract_errors.sh)
    rm -f /home/user/scripts/extract_errors.sh
    chmod 755 /home/user/scripts

    # Ensure errors directory is writable and empty (no .errors or error_summary.log)
    find /home/user/errors -type f -delete
    chmod 755 /home/user/errors
ENDPOST

WORKDIR /home/user
