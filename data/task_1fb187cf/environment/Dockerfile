FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create compliance directory and its files
mkdir -p /home/user/compliance

cat > /home/user/compliance/access_policy.yml << 'EOF'
policy: access
version: 1
rules:
  - deny_all_by_default: true
EOF

cat > /home/user/compliance/network_policy.yml << 'EOF'
policy: network
version: 2
rules:
  - block_inbound: true
  - allow_egress_443: true
EOF

cat > /home/user/compliance/secrets_policy.yml << 'EOF'
policy: secrets
version: 1
rules:
  - rotate_every_days: 90
  - min_length: 32
EOF

cat > /home/user/compliance/notes.txt << 'EOF'
TODO: review draft policies before merge
EOF

cat > /home/user/compliance/draft_network.yml << 'EOF'
policy: network-draft
version: 0
EOF

cat > /home/user/compliance/README.md << 'EOF'
# Compliance directory
Contains active and draft policy files.
EOF

# Do NOT create /home/user/backups or any output files — the agent will do that

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
