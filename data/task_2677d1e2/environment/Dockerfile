FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create migration directory
mkdir -p /home/user/migration

# Create the services.log file with the expected content
cat > /home/user/migration/services.log << 'EOF'
[2024-06-10 08:01:32] [SUCCESS] auth-service :: Migrated to us-east-2 successfully
[2024-06-10 08:03:11] [FAILED] billing-service :: Connection timeout during snapshot transfer
[2024-06-10 08:07:45] [SKIPPED] legacy-reporting :: Marked for decommission, skipping migration
[2024-06-10 08:09:02] [SUCCESS] user-profile-service :: All data synced and verified
[2024-06-10 08:11:58] [FAILED] api-gateway :: TLS certificate mismatch on target region
[2024-06-10 08:14:30] [SUCCESS] notification-service :: Migrated to us-east-2 successfully
[2024-06-10 08:17:44] [FAILED] data-pipeline :: Disk quota exceeded on destination bucket
[2024-06-10 08:20:05] [SKIPPED] internal-dashboard :: Dependency on legacy-reporting, skipping
[2024-06-10 08:23:19] [SUCCESS] search-service :: Migrated to us-east-2 successfully
[2024-06-10 08:26:52] [FAILED] payment-processor :: IAM role missing required S3 permissions
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
