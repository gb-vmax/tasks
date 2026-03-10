FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create finops group and analyst user
groupadd finops
useradd -M -s /bin/bash analyst

# Create directory structure
mkdir -p /home/user/finops/reports

# Create CSV files with expected content
printf "service,cost\nEC2,1200\nS3,340" > /home/user/finops/reports/q1_budget.csv
printf "service,cost\nEC2,1500\nRDS,890" > /home/user/finops/reports/q2_budget.csv
printf "service,cost\nLambda,200\nS3,410" > /home/user/finops/reports/q3_budget.csv

# Set ownership to user:user
chown user:user /home/user/finops/reports
chown user:user /home/user/finops/reports/q1_budget.csv
chown user:user /home/user/finops/reports/q2_budget.csv
chown user:user /home/user/finops/reports/q3_budget.csv

# Set permissions as required by initial state tests
chmod 755 /home/user/finops/reports
chmod 644 /home/user/finops/reports/q1_budget.csv
chmod 644 /home/user/finops/reports/q2_budget.csv
chmod 644 /home/user/finops/reports/q3_budget.csv

# Ensure /home/user is owned by user
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
