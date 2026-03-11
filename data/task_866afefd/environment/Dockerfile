FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the devsecops directory
mkdir -p /home/user/devsecops

# Create the accounts.json file with the required content
cat > /home/user/devsecops/accounts.json << 'EOF'
[
  {"name": "svc-deploy", "role": "deployer", "env": "production", "password_expires": false},
  {"name": "svc-monitor", "role": "readonly", "env": "production", "password_expires": true},
  {"name": "svc-backup", "role": "backup-agent", "env": "staging", "password_expires": false},
  {"name": "svc-ci", "role": "builder", "env": "staging", "password_expires": true},
  {"name": "svc-audit", "role": "auditor", "env": "production", "password_expires": true},
  {"name": "svc-infra", "role": "admin", "env": "production", "password_expires": false}
]
EOF

# Do NOT create violations.txt — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
