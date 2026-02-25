FROM ubuntu:22.04

RUN <<'ENDPOST'
set -eux

    apt-get update
    apt-get install -y python3 python3-pip

    # Install pytest
    pip3 install --no-cache-dir pytest

    # Create user and home directory if not present
    useradd -m user || true

    # Set up required directories
    mkdir -p /home/user/dashboards
    mkdir -p /home/user/envs/prod
    mkdir -p /home/user/envs/staging

    # Create prod_dashboard.json with required content
    cat > /home/user/dashboards/prod_dashboard.json <<EOF
{"env": "prod", "widgets": ["cpu", "memory", "network"]}
EOF

    # Create staging_dashboard.json with required content
    cat > /home/user/dashboards/staging_dashboard.json <<EOF
{"env": "staging", "widgets": ["cpu", "memory"]}
EOF

    # Set permissions so non-root user can modify files and directories
    chown -R user:user /home/user
    chmod -R u+rwX,go+rX /home/user
ENDPOST

WORKDIR /home/user
