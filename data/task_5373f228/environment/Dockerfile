FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/data

cat > /home/user/data/services.json << 'EOF'
[
  {"id": 1, "name": "api-gateway", "status": "healthy", "region": "us-east-1", "response_time_ms": 45, "owner_email": "ops@example.com"},
  {"id": 2, "name": "auth-service", "status": "degraded", "region": "us-west-2", "response_time_ms": 320, "owner_email": "security@example.com"},
  {"id": 3, "name": "billing-worker", "status": "healthy", "region": "eu-central-1", "response_time_ms": 88, "owner_email": "billing@example.com"},
  {"id": 4, "name": "notification-service", "status": "down", "region": "us-east-1", "response_time_ms": 9999, "owner_email": "infra@example.com"},
  {"id": 5, "name": "search-indexer", "status": "healthy", "region": "ap-southeast-1", "response_time_ms": 112, "owner_email": "search@example.com"}
]
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
