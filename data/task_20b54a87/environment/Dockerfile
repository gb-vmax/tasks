FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create directory structure
mkdir -p /home/user/mlops/experiments
mkdir -p /home/user/mlops/artifacts

# Create the initial run_42.yaml file
cat > /home/user/mlops/experiments/run_42.yaml << 'EOF'
experiment_name: gradient_boost_experiment
run_id: 42
status: "running"
model:
  type: gradient_boosting
  n_estimators: 200
  learning_rate: 0.05
  max_depth: 5
metrics:
  val_accuracy: null
  val_loss: null
  train_accuracy: 0.9512
EOF

# Create the initial registry.toml file
cat > /home/user/mlops/artifacts/registry.toml << 'EOF'
[[models]]
run_id = 39
name = "gradient_boost_v1"
status = "production"
val_accuracy = 0.8841
artifact_path = "s3://mlops-bucket/run_39/model.pkl"

[[models]]
run_id = 41
name = "gradient_boost_v2"
status = "archived"
val_accuracy = 0.9005
artifact_path = "s3://mlops-bucket/run_41/model.pkl"
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
