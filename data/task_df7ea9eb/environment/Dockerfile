FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the backups directory
mkdir -p /home/user/backups

# Create the nightly backup log file
cat > /home/user/backups/backup_nightly.log << 'EOF'
[2024-11-03 01:00:00] STARTED db_primary_backup
[2024-11-03 01:00:03] INFO Connecting to database host db01.internal
[2024-11-03 01:00:05] STARTED media_archive
[2024-11-03 02:14:37] COMPLETED db_primary_backup
[2024-11-03 02:14:40] WARNING Disk usage on backup target at 78%
[2024-11-03 02:31:05] COMPLETED media_archive
[2024-11-03 02:31:06] STARTED config_snapshot
[2024-11-03 02:31:10] INFO Snapshotting /etc and /home/user/.config
[2024-11-03 02:31:11] STARTED logs_offsite
[2024-11-03 02:33:44] FAILED logs_offsite
[2024-11-03 02:33:44] INFO Remote host unreachable, skipping offsite transfer
[2024-11-03 02:35:02] COMPLETED config_snapshot
[2024-11-03 02:35:03] STARTED userdata_weekly
[2024-11-03 03:58:21] COMPLETED userdata_weekly
[2024-11-03 03:58:25] INFO All jobs finished
EOF

# Do NOT create archive_summary.txt — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
