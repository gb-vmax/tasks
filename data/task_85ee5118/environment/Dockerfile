FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin

RUN <<'ENDPOST'
set -eux

# Create user and home directory
useradd -m user
mkdir -p /home/user/k8s-manifests/current

# Create three manifest files in /home/user/k8s-manifests/
echo "# frontend deployment manifest" > /home/user/k8s-manifests/frontend-deployment.yaml
echo "# backend deployment manifest" > /home/user/k8s-manifests/backend-deployment.yaml
echo "# database deployment manifest" > /home/user/k8s-manifests/database-deployment.yaml

# Ensure permissions allow non-root user access
chown -R user:user /home/user
chmod -R 755 /home/user

# Install pip and pytest
apt-get update
apt-get install -y python3-pip
pip3 install pytest
ENDPOST

WORKDIR /home/user
