FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
# Do NOT run the solution or create output files

# Create required directories
install -d -m 755 /home/user/backup_logs
install -d -m 755 /home/user/backup_scripts
install -d -m 755 /home/user/backup_summary

# Create backup log files with specified contents
cat > /home/user/backup_logs/backup_20240618.log <<EOF
[2024-06-18 01:41:00] INFO: Database backup completed: customer_data (Duration: 00:15:01) - STATUS: FAILURE
[2024-06-18 01:43:00] INFO: Database backup completed: customer_data (Duration: 00:12:03) - STATUS: SUCCESS
EOF

cat > /home/user/backup_logs/backup_20240619.log <<EOF
[2024-06-19 00:03:13] INFO: Database backup completed: other_db (Duration: 00:05:00) - STATUS: SUCCESS
[2024-06-19 01:43:01] INFO: Database backup completed: customer_data (Duration: 00:07:20) - STATUS: FAILURE
EOF

cat > /home/user/backup_logs/backup_20240620.log <<EOF
[2024-06-20 01:44:15] INFO: Database backup completed: customer_data (Duration: 00:13:55) - STATUS: SUCCESS
EOF

cat > /home/user/backup_logs/backup_20240621.log <<EOF
[2024-06-21 01:41:27] INFO: Database backup completed: customer_data (Duration: 00:11:57) - STATUS: FAILURE
[2024-06-21 01:44:28] INFO: Database backup completed: customer_data (Duration: 00:09:40) - STATUS: SUCCESS
EOF

cat > /home/user/backup_logs/backup_20240622.log <<EOF
[2024-06-22 00:35:22] INFO: Database backup completed: customer_data (Duration: 00:08:32) - STATUS: FAILURE
EOF

# Create the backup script and make it executable
echo "#!/bin/bash" > /home/user/backup_scripts/postgres_backup.sh
chmod 755 /home/user/backup_scripts/postgres_backup.sh

# Ensure correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
