FROM ubuntu:22.04

RUN <<'ENDPOST'
set -eux

    # Create user and home directory if not exists
    useradd -m -s /bin/bash user || true

    # Ensure /home/user exists and is owned by user
    mkdir -p /home/user
    chown user:user /home/user

    # Create artifact_names.txt with exact required content
    cat > /home/user/artifact_names.txt <<'EOF'
model_v1.pt
metrics.json
training.log
model_v1.pt
metrics.json
model_v2.pt
model_v1.pt
metrics.json
model_v2.pt
model_v1.pt
training.log
config.yaml
EOF

    # Set correct ownership and permissions for the file
    chown user:user /home/user/artifact_names.txt
    chmod 644 /home/user/artifact_names.txt

    # Install pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest
ENDPOST

WORKDIR /home/user
