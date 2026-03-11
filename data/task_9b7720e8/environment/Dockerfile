FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/ml_project

cat > /home/user/ml_project/raw_samples.csv << 'EOF'
sample_id,feature1,feature2,label
s001,1.5,-2.3,0
s002,9.9,10.0,1
s003,,3.1,0
s004,11.2,0.5,1
s005,-3.3,-11.0,0
s006,0.0,0.0,2
s007,2.7,abc,1
s008,-10.0,10.0,0
s009,5.5,5.5,
s010,4.2,3.8,1
EOF

# Remove trailing newline to match expected content exactly
truncate -s -1 /home/user/ml_project/raw_samples.csv

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
