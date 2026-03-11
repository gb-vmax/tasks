FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the data directory
mkdir -p /home/user/data

# Create the sales.csv input file
cat > /home/user/data/sales.csv << 'EOF'
transaction_id,date,region,product_code,amount,status
T001,2024-01-05,north,PRD-001,150.00,completed
T002,2024-01-06,south,PRD-10,89.50,completed
T003,2024-01-07,east,PRD-042,200.00,pending
T004,2024-01-08,west,PRD-007,310.75,completed
T005,2024-01-09,north,PRD-1234,45.00,completed
T006,2024-01-10,south,PRD-099,99.99,refunded
T007,2024-01-11,east,PRD-003,55.25,cancelled
T008,2024-01-12,west,PRD-88,175.00,refunded
T009,2024-01-13,north,PRD-056,420.00,Completed
T010,2024-01-14,south,PRD-002,60.00,refunded
T011,2024-01-15,east,PRD-777,130.00,completed
T012,2024-01-16,west,PRD-019,88.40,pending
T013,2024-01-17,north,PRD-500,250.00,completed
T014,2024-01-18,south,PRD-AB1,190.00,completed
T015,2024-01-19,east,PRD-011,75.00,refunded
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
