FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the audit log directory structure
mkdir -p /home/user/audit_logs/2024-02

# Create auth.log
cat > /home/user/audit_logs/2024-02/auth.log << 'EOF'
2024-02-01 00:00:01 USER login success admin
2024-02-01 00:05:33 USER login failure jsmith
2024-02-01 00:07:12 USER login success jsmith
2024-02-28 23:59:59 USER logout admin
EOF

# Create access.log
cat > /home/user/audit_logs/2024-02/access.log << 'EOF'
2024-02-01 08:00:00 READ /reports/q4.pdf admin
2024-02-01 08:15:22 WRITE /reports/q4.pdf admin
2024-02-15 14:30:00 READ /reports/q4.pdf jsmith
2024-02-28 17:45:00 DELETE /tmp/scratch.txt admin
EOF

# Create changes.log
cat > /home/user/audit_logs/2024-02/changes.log << 'EOF'
2024-02-03 09:00:00 CONFIG changed firewall rules by admin
2024-02-10 11:22:45 PERMISSION granted jsmith access to /reports
2024-02-20 16:00:00 USER created bwilson by admin
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
