FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin:$PATH

RUN <<'ENDPOST'
set -e

    # Install Python3, pip, and PyYAML (for YAML parsing if needed)
    apt-get update
    apt-get install -y python3 python3-pip
    pip3 install --no-cache-dir pytest

    # Create the user and home directory if not present
    useradd -m -s /bin/bash user || true

    # Create the k8s_manifests directory with correct permissions
    mkdir -p /home/user/k8s_manifests
    chown user:user /home/user/k8s_manifests

    # Write frontend.yaml
    cat > /home/user/k8s_manifests/frontend.yaml <<'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
        - name: frontend-container
          image: nginx:1.19
EOF

    # Write backend.yaml
    cat > /home/user/k8s_manifests/backend.yaml <<'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
spec:
  replicas: 2
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
        - name: backend-container
          image: python:3.9
EOF

    # Write database.yaml
    cat > /home/user/k8s_manifests/database.yaml <<'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: database
spec:
  replicas: 1
  selector:
    matchLabels:
      app: database
  template:
    metadata:
      labels:
        app: database
    spec:
      containers:
        - name: database-container
          image: mongo:4.4
EOF

    # Set ownership to user for all files
    chown user:user /home/user/k8s_manifests/*.yaml
ENDPOST

WORKDIR /home/user
