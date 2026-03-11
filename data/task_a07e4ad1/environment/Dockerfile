FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the logs directory with the required log files
mkdir -p /home/user/logs

# Create January 2024 log files
cat > /home/user/logs/app-2024-01-01.log << 'EOF'
2024-01-01 00:00:01 INFO Service started
2024-01-01 08:32:11 ERROR Disk quota exceeded
EOF

cat > /home/user/logs/app-2024-01-15.log << 'EOF'
2024-01-15 14:22:05 WARN Connection timeout
2024-01-15 14:22:10 INFO Reconnected
EOF

cat > /home/user/logs/app-2024-01-31.log << 'EOF'
2024-01-31 23:59:59 INFO Scheduled maintenance
EOF

# Create February 2024 log file (should be excluded from archive)
cat > /home/user/logs/app-2024-02-01.log << 'EOF'
2024-02-01 09:00:00 INFO Service started
EOF

# Create system log (should be excluded from archive)
cat > /home/user/logs/system.log << 'EOF'
kernel: [0.000000] Booting Linux
EOF

# Do NOT create /home/user/backups — the agent must create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
