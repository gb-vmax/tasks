FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/finops

cat > /home/user/finops/resources.csv << 'EOF'
resource_id,service,region,monthly_cost_usd
i-0a1b2c3d,EC2,us-east-1,72.50
i-0b2c3d4e,EC2,us-west-2,118.30
db-0c3d4e5f,RDS,us-east-1,210.00
db-0d4e5f6g,RDS,eu-west-1,95.75
s3-0e5f6g7h,S3,us-east-1,14.40
i-0f6g7h8i,EC2,ap-southeast-1,43.20
s3-0g7h8i9j,S3,us-west-2,8.90
db-0h8i9j0k,RDS,us-east-1,140.00
i-0i9j0k1l,EC2,eu-west-1,31.75
s3-0j0k1l2m,S3,us-east-1,22.15
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
