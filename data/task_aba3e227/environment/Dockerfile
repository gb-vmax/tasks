FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the cloud directory
mkdir -p /home/user/cloud

# Create the services.csv input file
cat > /home/user/cloud/services.csv << 'EOF'
service_name,region,tier,monthly_cost_usd,replicas
auth-service,us-east-1,production,1200,3
image-processor,eu-west-2,production,800,2
billing-api,us-east-1,production,2400,5
logging-agent,us-east-1,staging,150,1
search-service,us-east-1,production,3100,4
cache-cluster,ap-south-1,production,950,3
notification-svc,us-east-1,staging,200,2
data-pipeline,us-east-1,production,4500,6
gateway-api,eu-west-2,production,1100,3
queue-worker,us-east-1,production,750,2
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
