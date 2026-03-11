FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create deployment directory structure
mkdir -p /home/user/deployments/app
mkdir -p /home/user/deployments/db
mkdir -p /home/user/deployments/gateway

# Create app/service.conf (contains old key)
cat > /home/user/deployments/app/service.conf << 'EOF'
[service]
name=payment-api
api_key=sk-OLDKEY-v1-abc123def456
timeout=30
EOF

# Create app/worker.conf (no old key)
cat > /home/user/deployments/app/worker.conf << 'EOF'
[worker]
name=background-worker
max_retries=5
log_level=info
EOF

# Create db/primary.conf (contains old key)
cat > /home/user/deployments/db/primary.conf << 'EOF'
[database]
host=db.internal
port=5432
api_key=sk-OLDKEY-v1-abc123def456
pool_size=10
EOF

# Create db/replica.conf (no old key)
cat > /home/user/deployments/db/replica.conf << 'EOF'
[database]
host=replica.internal
port=5432
pool_size=5
readonly=true
EOF

# Create gateway/proxy.conf (contains old key)
cat > /home/user/deployments/gateway/proxy.conf << 'EOF'
[proxy]
upstream=backend:8080
api_key=sk-OLDKEY-v1-abc123def456
tls=true
retries=3
EOF

# Create gateway/tls.conf (no old key)
cat > /home/user/deployments/gateway/tls.conf << 'EOF'
[tls]
cert=/etc/ssl/certs/service.crt
key=/etc/ssl/private/service.key
protocols=TLSv1.2,TLSv1.3
EOF

# Do NOT create rotation_audit.log — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
