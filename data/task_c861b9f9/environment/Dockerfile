FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/services/input
mkdir -p /home/user/services/output

cat > /home/user/services/input/services.csv <<EOF
service_name,image,exposed_port
auth-service,registry.example.com/auth:1.0,5000
user-service,registry.example.com/user:1.2,5001
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
