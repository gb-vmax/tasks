FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin

RUN <<'ENDPOST'
set -eux

    # Install Python 3 and pip (required by pytest)
    apt-get update
    apt-get install -y python3 python3-pip

    # Install pytest
    pip3 install --no-cache-dir pytest

    # Create user and home directory if not already present
    useradd -m user || true

    # Ensure /home/user exists and is owned by user
    mkdir -p /home/user
    chown user:user /home/user

    # Create the k8s_pods.json file with the specified content
    cat > /home/user/k8s_pods.json <<'EOF'
{
  "pods": [
    {"name": "nginx-7fdc69b969-abcde", "status": "Running"},
    {"name": "api-56bf4df57-uvwxy", "status": "Pending"},
    {"name": "db-0", "status": "Running"},
    {"name": "cache-0", "status": "CrashLoopBackOff"},
    {"name": "nginx-7fdc69b969-fghij", "status": "Running"}
  ]
}
EOF

    # Ensure permissions are correct
    chown user:user /home/user/k8s_pods.json
    chmod 644 /home/user/k8s_pods.json
ENDPOST

WORKDIR /home/user
