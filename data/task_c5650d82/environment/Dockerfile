FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/automation

cat > /home/user/automation/workflow_runs.log << 'EOF'
sync_users
deploy_prod
backup_db
sync_users
notify_slack
deploy_prod
sync_users
backup_db
deploy_prod
notify_slack
sync_users
deploy_prod
run_tests
sync_users
deploy_prod
backup_db
notify_slack
sync_users
deploy_prod
run_tests
sync_users
deploy_prod
notify_slack
backup_db
sync_users
deploy_prod
run_tests
sync_users
deploy_prod
notify_slack
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
