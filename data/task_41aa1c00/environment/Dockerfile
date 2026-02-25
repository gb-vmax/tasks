FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin:$PATH

RUN <<'ENDPOST'
set -e

    # Install python3 and pip
    apt-get update
    apt-get install -y python3 python3-pip

    # Install pytest
    pip3 install pytest

    # Create user and home directory if not already present
    if ! id user >/dev/null 2>&1; then
        useradd -m -s /bin/bash user
    fi

    # Prepare the directory structure
    mkdir -p /home/user/observability/dashboard_config

    # Set up dashboard_metrics.yaml with correct initial content
    cat > /home/user/observability/dashboard_config/dashboard_metrics.yaml <<'EOF'
metrics:
  cpu: usage
  memory: usage
# Dashboard refresh interval (update as needed)
refresh_interval: 30s
EOF

    # Set up audit.log with correct initial content
    cat > /home/user/observability/dashboard_config/audit.log <<'EOF'
[2024-06-23 10:03:55] alice: Created dashboard_metrics.yaml
[2024-06-23 10:10:02] bob: Edited dashboard_metrics.yaml
EOF

    # Set permissions so user can read/write all files and directories
    chown -R user:user /home/user/observability
    chmod -R u+rwX,go+rX /home/user/observability
ENDPOST

WORKDIR /home/user
