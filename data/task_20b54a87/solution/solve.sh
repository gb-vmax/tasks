#!/bin/bash
set -e
cd /home/user

cat /home/user/mlops/experiments/run_42.yaml
cat /home/user/mlops/artifacts/registry.toml
sed -i 's/status: "running"/status: "completed"/' /home/user/mlops/experiments/run_42.yaml && sed -i 's/  val_accuracy: null/  val_accuracy: 0.9173/' /home/user/mlops/experiments/run_42.yaml && sed -i 's/  val_loss: null/  val_loss: 0.2041/' /home/user/mlops/experiments/run_42.yaml && echo 'artifact_path: "s3://mlops-bucket/run_42/model.pkl"' >> /home/user/mlops/experiments/run_42.yaml
cat /home/user/mlops/experiments/run_42.yaml
printf '\n[[models]]\nrun_id = 42\nname = "gradient_boost_v3"\nstatus = "staged"\nval_accuracy = 0.9173\nartifact_path = "s3://mlops-bucket/run_42/model.pkl"\n' >> /home/user/mlops/artifacts/registry.toml
cat /home/user/mlops/artifacts/registry.toml
