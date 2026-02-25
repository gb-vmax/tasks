FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin:$PATH

RUN <<'ENDPOST'
set -e

    # Create user and home directory if not present
    if ! id user 2>/dev/null; then
        useradd -m -s /bin/bash user
    fi

    # Create the profile_data directory as user (so permissions are correct)
    mkdir -p /home/user/profile_data
    chown user:user /home/user/profile_data

    # Create the app_memory.csv file with required contents
    cat > /home/user/profile_data/app_memory.csv <<'EOF'
application,timestamp,rss_MB
renderer,2024-06-01T09:00:00,180
indexer,2024-06-01T09:00:00,120
renderer,2024-06-01T09:05:00,195
indexer,2024-06-01T09:05:00,135
renderer,2024-06-01T09:15:00,178
EOF

    chown user:user /home/user/profile_data/app_memory.csv
    chmod 644 /home/user/profile_data/app_memory.csv

    # Do not create the output JSON file; it should not exist before the task

    # Update and install Python3, pip, and pytest
    apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        python3 \
        python3-pip

    pip3 install --no-cache-dir pytest
ENDPOST

WORKDIR /home/user
