FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the artifact-manager base directory
mkdir -p /home/user/artifact-manager

# Create the repos.conf configuration file
cat > /home/user/artifact-manager/repos.conf << 'EOF'
libs-release:maven:90
libs-snapshot:maven:14
docker-local:docker:30
pypi-internal:pypi:60
raw-binaries:generic:180
EOF

# Do NOT create the storage directory or MANIFEST file — the agent must do that

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
