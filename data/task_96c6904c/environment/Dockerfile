FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/data

cat > /home/user/data/raw_samples.csv << 'EOF'
sample_id,feature_a,feature_b,feature_c,label,split
S001,0.12,0.87,0.45,positive,train
S002,0.93,0.11,0.76,negative,test
S003,0.55,1.20,0.88,positive,train
S004,0.37,0.64,0.29,negative,val
S005,0.81,0.45,0.63,negative,train
S006,0.22,0.99,0.14,positive,test
S007,0.68,0.33,0.91,positive,train
S008,0.44,0.77,0.55,negative,val
S009,0.09,0.52,0.38,negative,train
S010,0.76,0.18,0.82,positive,test
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
