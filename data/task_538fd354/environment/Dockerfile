FROM endless-deps-c84d384f2a25:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the deployments directory
mkdir -p /home/user/deployments

# Create the manifest.json file
cat > /home/user/deployments/manifest.json << 'EOF'
[
  {
    "service": "auth-service",
    "version": "2.3.1",
    "environment": "production",
    "status": "ready",
    "replicas": 4,
    "owner": "platform-team"
  },
  {
    "service": "billing-service",
    "version": "1.8.0",
    "environment": "staging",
    "status": "ready",
    "replicas": 2,
    "owner": "payments-team"
  },
  {
    "service": "user-service",
    "version": "3.1.4",
    "environment": "production",
    "status": "pending",
    "replicas": 6,
    "owner": "core-team"
  },
  {
    "service": "notification-service",
    "version": "1.2.9",
    "environment": "production",
    "status": "ready",
    "replicas": 3,
    "owner": "platform-team"
  },
  {
    "service": "search-service",
    "version": "4.0.2",
    "environment": "production",
    "status": "failed",
    "replicas": 5,
    "owner": "search-team"
  },
  {
    "service": "analytics-service",
    "version": "2.0.0",
    "environment": "production",
    "status": "ready",
    "replicas": 2,
    "owner": "data-team"
  }
]
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
