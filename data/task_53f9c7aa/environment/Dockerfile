FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/mlops

cat > /home/user/mlops/artifact_log.txt << 'EOF'
model_checkpoint
confusion_matrix
model_checkpoint
training_log
model_checkpoint
roc_curve
confusion_matrix
model_checkpoint
training_log
feature_importance
model_checkpoint
confusion_matrix
roc_curve
model_checkpoint
training_log
model_checkpoint
confusion_matrix
feature_importance
model_checkpoint
roc_curve
training_log
model_checkpoint
confusion_matrix
model_checkpoint
feature_importance
model_checkpoint
roc_curve
training_log
confusion_matrix
model_checkpoint
training_log
feature_importance
model_checkpoint
confusion_matrix
roc_curve
model_checkpoint
training_log
confusion_matrix
model_checkpoint
feature_importance
roc_curve
model_checkpoint
training_log
confusion_matrix
model_checkpoint
roc_curve
feature_importance
model_checkpoint
training_log
confusion_matrix
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
