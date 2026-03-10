FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the ml_data directory
mkdir -p /home/user/ml_data

# Create the raw CSV input file
cat > /home/user/ml_data/raw_samples.csv << 'EOF'
sample_id,feature_a,feature_b,quality_score,label
3,0.512,1.837,0.91,cat
7,1.204,0.334,0.60,dog
12,2.871,3.142,0.88,cat
5,0.099,2.201,0.74,dog
19,1.553,0.778,0.77,unknown
1,3.400,1.020,0.82,dog
8,0.761,4.112,0.95,cat
15,2.233,0.541,0.69,cat
22,1.847,2.930,0.78,dog
10,0.314,0.628,0.80,unknown
6,1.111,1.111,0.76,cat
EOF

# Do NOT create training_ready.csv — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
