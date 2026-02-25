#!/bin/bash
set -e
cd /home/user

# Create the tar.gz archive with just the log files at the root (no directory paths)
# Use a temporary directory to stage the files for clean archive paths
TMPSTAGE=$(mktemp -d)
cp microservices/auth/auth.log "$TMPSTAGE/"
cp microservices/payment/payment.log "$TMPSTAGE/"
tar czf logs_backup.tar.gz -C "$TMPSTAGE" auth.log payment.log
rm -rf "$TMPSTAGE"

# Create the restore directory and extract
mkdir -p logs_restore
tar xzf logs_backup.tar.gz -C logs_restore

# Create the restore report
cat > logs_restore/restore_report.txt << 'EOF'
Restored Files:
auth.log
payment.log
EOF
