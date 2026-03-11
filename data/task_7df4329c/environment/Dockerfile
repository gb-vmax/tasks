FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the audit_logs directory
mkdir -p /home/user/audit_logs

# Create March 2024 log files
cat > /home/user/audit_logs/access_2024-03-01.log << 'EOF'
2024-03-01 08:01:12 user=alice action=LOGIN ip=10.0.0.1
2024-03-01 08:45:33 user=bob action=READ_RECORD ip=10.0.0.2
EOF

cat > /home/user/audit_logs/access_2024-03-08.log << 'EOF'
2024-03-08 09:10:05 user=alice action=UPDATE_RECORD ip=10.0.0.1
2024-03-08 11:22:44 user=carol action=LOGIN ip=10.0.0.5
EOF

cat > /home/user/audit_logs/access_2024-03-15.log << 'EOF'
2024-03-15 13:05:17 user=bob action=DELETE_RECORD ip=10.0.0.2
2024-03-15 14:30:00 user=alice action=LOGOUT ip=10.0.0.1
EOF

cat > /home/user/audit_logs/access_2024-03-22.log << 'EOF'
2024-03-22 07:55:00 user=carol action=READ_RECORD ip=10.0.0.5
2024-03-22 08:10:20 user=dave action=LOGIN ip=10.0.0.9
EOF

cat > /home/user/audit_logs/access_2024-03-29.log << 'EOF'
2024-03-29 16:00:01 user=dave action=UPDATE_RECORD ip=10.0.0.9
2024-03-29 17:45:59 user=bob action=LOGOUT ip=10.0.0.2
EOF

# Create non-March files (should NOT be included in archive)
cat > /home/user/audit_logs/access_2024-02-28.log << 'EOF'
2024-02-28 10:00:00 user=alice action=LOGIN ip=10.0.0.1
EOF

cat > /home/user/audit_logs/access_2024-04-01.log << 'EOF'
2024-04-01 09:00:00 user=carol action=LOGIN ip=10.0.0.5
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
