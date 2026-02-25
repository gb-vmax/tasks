FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/devops
cat > /home/user/devops/requirements.txt <<EOF
flask==2.0.1
requests==2.26.0
EOF
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
