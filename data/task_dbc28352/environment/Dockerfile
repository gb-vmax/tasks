FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the devsecops directory
mkdir -p /home/user/devsecops

# Create the pod_configs.csv file with the expected content
cat > /home/user/devsecops/pod_configs.csv << 'EOF'
pod_name,namespace,image,privileged,run_as_root
api-server,production,myrepo/api:1.2,false,false
debug-shell,kube-system,busybox:latest,true,true
nginx-proxy,frontend,nginx:1.21,false,false
log-collector,monitoring,fluentd:v1.14,true,false
db-migrator,production,postgres:14,false,true
privileged-agent,infra,agent:3.0,true,false
cert-manager,cert-manager,quay.io/cert-manager:v1.9,false,false
node-exporter,monitoring,prom/node-exporter:v1.3,false,false
EOF

# Do NOT create violations.txt — the agent will generate it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
