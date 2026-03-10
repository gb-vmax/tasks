FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create data directory
mkdir -p /home/user/data

# Create the training CSV file
cat > /home/user/data/training_samples.csv << 'EOF'
sample_id,age,income,score,label
1,23,45000,88,1
2,35,62000,91,0
3,,54000,76,1
4,41,78000,,0
5,29,,83,1
6,52,91000,95,0
7,38,67000,72,1
8,,83000,84,0
9,31,59000,,1
10,44,72000,90,0
EOF

# Ensure report file does NOT exist
rm -f /home/user/data/dataset_report.txt

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
