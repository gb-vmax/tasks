FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/provisioning

cat > /home/user/provisioning/provision.sh << 'EOF'
#!/bin/bash

CONFIG=$1

if [ -z "$CONFIG" ]; then
  echo "Usage: provision.sh <config>" >&2
  exit 1
fi

source "$CONFIG"

echo "[START] Provisioning environment: $ENV in $REGION"
echo "[INFO] Services to provision: $SERVICES"

IFS=',' read -ra SERVICE_LIST <<< "$SERVICES"
for svc in "${SERVICE_LIST[@]}"; do
  echo "[INFO] Setting up $svc..."
  echo "[DONE] $svc provisioned successfully"
done

echo "[END] All services provisioned"
EOF

# Explicitly NOT making it executable (test requires it to not be executable)
chmod 644 /home/user/provisioning/provision.sh

cat > /home/user/provisioning/env.conf << 'EOF'
ENV=staging
REGION=us-east-1
SERVICES=nginx,postgres,redis
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
