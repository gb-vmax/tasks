FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/finops

cat > /home/user/finops/charges.csv << 'EOF'
r-0a1b2c,EC2,us-east-1,platform,142.50
r-0d4e5f,S3,eu-west-1,data,18.00
r-1a2b3c,RDS,us-west-2,analytics,95.00
r-2c3d4e,EC2,us-east-1,platform,200.00
r-3e4f5a,Lambda,ap-south-1,data,5.50
r-4f5a6b,S3,us-east-1,infra,12.00
r-5b6c7d,EC2,eu-west-1,analytics,310.00
r-6d7e8f,RDS,us-east-1,platform,450.00
r-7e8f9a,CloudFront,us-east-1,data,33.00
r-8f9a0b,EC2,us-west-2,platform,175.00
r-9a0b1c,S3,eu-west-1,analytics,8.00
r-a0b1c2,Lambda,us-east-1,platform,2.50
r-b1c2d3,EC2,ap-south-1,infra,88.00
r-c2d3e4,RDS,us-east-1,data,210.00
r-d3e4f5,EC2,us-east-1,platform,99.00
r-e4f5a6,S3,us-west-2,analytics,14.00
r-f5a6b7,EC2,eu-west-1,platform,321.00
r-a6b7c8,Lambda,us-east-1,data,7.00
r-b7c8d9,RDS,ap-south-1,platform,130.00
r-c8d9e0,EC2,us-east-1,analytics,265.00
r-d9e0f1,S3,eu-west-1,infra,19.50
r-e0f1a2,EC2,us-west-2,platform,410.00
r-f1a2b3,CloudFront,us-east-1,analytics,55.00
r-a2b3c4,Lambda,us-east-1,platform,3.00
r-b3c4d5,S3,ap-south-1,data,22.00
r-c4d5e6,EC2,us-east-1,platform,187.00
r-d5e6f7,RDS,eu-west-1,analytics,140.00
r-e6f7a8,EC2,us-west-2,platform,95.00
r-f7a8b9,S3,us-east-1,data,11.00
r-a8b9c0,Lambda,ap-south-1,infra,6.00
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
