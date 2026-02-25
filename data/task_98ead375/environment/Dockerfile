FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

# Create the containers directory and inventory.csv with required contents
mkdir -p /home/user/containers
cat > /home/user/containers/inventory.csv <<EOF
container_name,image_source
frontend,registry.corporate.com/frontend:2.1
backend,registry.corporate.com/backend:3.4
devops-tool,docker.io/library/devops-tool:latest
testservice,quay.io/example/testservice:1.1
EOF

# Create the output directory (no report file yet)
mkdir -p /home/user/output

# Ensure correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
