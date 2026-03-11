FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/finops

cat > /home/user/finops/aws_costs.csv << 'EOF'
region,service,account_id,cost_usd,usage_hours,team
us-east-1,EC2,123456789012,412.50,1200,platform
us-west-2,S3,123456789012,18.75,0,platform
eu-west-1,RDS,987654321098,930.00,720,data
ap-southeast-1,Lambda,555000111222,7.30,45000,backend
us-east-1,CloudFront,987654321098,53.20,0,frontend
eu-central-1,EC2,555000111222,601.80,1800,data
us-west-2,DynamoDB,123456789012,144.00,0,backend
ap-northeast-1,S3,987654321098,22.10,0,frontend
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
