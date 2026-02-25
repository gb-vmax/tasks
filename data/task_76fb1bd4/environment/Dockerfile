FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
install -d -m 0755 /home/user/releases
cat > /home/user/releases/service_list.csv <<EOF
service_name,current_version,next_version,maintainer
auth-service,1.4.2,1.5.0,alice
billing-service,2.9.0,3.0.0,bob
inventory-service,0.5.6,0.6.0,charlie
EOF
# Do NOT create deployments/ directory or deployment_manifest.log
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
