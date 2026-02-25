FROM ubuntu:22.04

ENV PATH=/home/user/.local/bin:$PATH

RUN <<'ENDPOST'
set -eux

    # Create user and home directory if not already present
    if ! id -u user >/dev/null 2>&1; then
        useradd -m -s /bin/bash user
    fi

    # Ensure /home/user exists and is owned by user
    mkdir -p /home/user
    chown user:user /home/user

    # Create the k8s-manifests directory and set permissions
    mkdir -p /home/user/k8s-manifests
    chown user:user /home/user/k8s-manifests
    chmod 700 /home/user/k8s-manifests

    # Create deployments.csv with exact required content
    cat > /home/user/k8s-manifests/deployments.csv <<'EOF'
name,namespace,image,replicas
frontend,default,nginx:1.20,3
backend,prod,backend-app:2.1,2
analytics,default,my-analytics:0.4,1
EOF

    chown user:user /home/user/k8s-manifests/deployments.csv
    chmod 600 /home/user/k8s-manifests/deployments.csv

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip python3-setuptools
    pip3 install --no-cache-dir pytest
ENDPOST

WORKDIR /home/user
