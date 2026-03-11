FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the pipelines directory
mkdir -p /home/user/pipelines

# Create the .yml files
cat > /home/user/pipelines/build.yml << 'EOF'
stages:
  - build
  - test
EOF

cat > /home/user/pipelines/deploy.yml << 'EOF'
stages:
  - deploy
environment: production
EOF

cat > /home/user/pipelines/notify.yml << 'EOF'
on_success: slack
on_failure: pagerduty
EOF

# Create the non-yml files
cat > /home/user/pipelines/README.txt << 'EOF'
Pipeline configurations for the main repo.
EOF

cat > /home/user/pipelines/debug.log << 'EOF'
2024-01-10 12:00:00 pipeline started
EOF

# Do NOT create /home/user/artifacts/ — the agent must create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
