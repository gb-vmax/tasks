FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the audit directory
mkdir -p /home/user/audit

# Create the events CSV file with the required content
cat > /home/user/audit/events.csv << 'EOF'
timestamp_utc,user,action,resource
2024-06-15T08:00:00Z,alice,LOGIN,portal
2024-06-15T13:30:00Z,bob,DOWNLOAD,report_q2.pdf
2024-06-15T14:15:00Z,alice,UPLOAD,config_backup.tar
2024-06-15T19:45:00Z,carol,LOGIN,portal
2024-06-15T21:00:00Z,bob,LOGOUT,portal
2024-06-15T23:30:00Z,alice,DELETE,temp_logs.zip
EOF

# Do NOT create audit_report.txt or system_audit.log — the agent will create those

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
