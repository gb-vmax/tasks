FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
ML_DIR="/home/user/ml_experiments"
EXP_DIR="$ML_DIR/exp_42"

# Create directories
mkdir -p "$EXP_DIR/model"
mkdir -p "$EXP_DIR/logs"

# Create model/model.h5 (binary file, 9112 bytes, placeholder content)
head -c 9112 </dev/urandom >"$EXP_DIR/model/model.h5"

# Create model/params.json with required content
cat >"$EXP_DIR/model/params.json" <<EOF
{"layers": 3, "units": 128, "activation": "relu"}
EOF

# Create logs/train.log with required content
cat >"$EXP_DIR/logs/train.log" <<EOF
Epoch 1/10 - loss: 0.23
Epoch 2/10 - loss: 0.19
EOF

# Create metrics.csv with required content
cat >"$EXP_DIR/metrics.csv" <<EOF
epoch,accuracy,loss
1,0.865,0.23
2,0.890,0.19
EOF

# Ensure permissions/ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
