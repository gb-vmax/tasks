FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create directory structure
mkdir -p /home/user/finops/reports/2024-06
mkdir -p /home/user/finops/reports/current

# Create AWS CSV file
cat > /home/user/finops/reports/2024-06/aws_costs_2024-06.csv << 'EOF'
service,cost_usd
EC2,1200.50
S3,340.20
RDS,890.00
EOF

# Create GCP CSV file
cat > /home/user/finops/reports/2024-06/gcp_costs_2024-06.csv << 'EOF'
service,cost_usd
Compute Engine,980.75
Cloud Storage,210.40
BigQuery,560.10
EOF

# Create Azure CSV file
cat > /home/user/finops/reports/2024-06/azure_costs_2024-06.csv << 'EOF'
service,cost_usd
Virtual Machines,1050.30
Blob Storage,175.60
Azure SQL,720.90
EOF

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
