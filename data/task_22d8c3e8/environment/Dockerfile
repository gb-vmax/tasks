FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the infra directory
mkdir -p /home/user/infra

# Create the servers.csv inventory file
cat > /home/user/infra/servers.csv << 'EOF'
hostname,ip_address,environment,status,role
web-prod-01,10.0.1.10,prod,unprovisioned,webserver
web-prod-02,10.0.1.11,prod,running,webserver
db-prod-01,10.0.2.10,prod,unprovisioned,database
app-staging-01,10.0.3.10,staging,unprovisioned,appserver
app-prod-01,10.0.1.20,prod,running,appserver
cache-prod-01,10.0.1.30,prod,unprovisioned,cache
db-staging-01,10.0.3.20,staging,unprovisioned,database
lb-prod-01,10.0.1.5,prod,stopped,loadbalancer
worker-prod-01,10.0.1.40,prod,unprovisioned,worker
EOF

# Do NOT create provision_targets.ini — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
