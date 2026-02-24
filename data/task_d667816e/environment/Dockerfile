FROM ubuntu:22.04

ENV PATH=/home/user/.local/bin:$PATH

RUN <<'ENDPOST'
set -e

    # Install Python3, pip, and PyYAML (for YAML validation in workflow)
    apt-get update
    apt-get install -y python3 python3-pip

    # Install pytest for testing
    pip3 install --no-cache-dir pytest

    # Create the user and home directory if not already present
    useradd -m -d /home/user user || true
    mkdir -p /home/user/old-operator

    # Set up the initial deployment.yaml
    cat > /home/user/old-operator/deployment.yaml <<'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: old-app-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: old-app
  template:
    metadata:
      labels:
        app: old-app
    spec:
      containers:
      - name: old-app-container
        image: old-app-image:v1.2.3
        ports:
        - containerPort: 80
EOF

    # Set up the initial service.yaml
    cat > /home/user/old-operator/service.yaml <<'EOF'
apiVersion: v1
kind: Service
metadata:
  name: old-app-service
spec:
  selector:
    app: old-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: ClusterIP
EOF

    # Ensure correct permissions for the user
    chown -R user:user /home/user/old-operator
ENDPOST

WORKDIR /home/user
