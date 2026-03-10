FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create incident directory structure
mkdir -p /home/user/incident/logs

# Create .error log files
cat > /home/user/incident/logs/app.error << 'EOF'
[ERROR] 2024-06-01 08:12:33 Application crashed: null pointer dereference
[ERROR] 2024-06-01 08:12:34 Stack trace: main.c:422
EOF

cat > /home/user/incident/logs/db.error << 'EOF'
[ERROR] 2024-06-01 08:13:01 Database connection timeout after 30s
[ERROR] 2024-06-01 08:13:05 Retry 1 of 3 failed
EOF

cat > /home/user/incident/logs/nginx.error << 'EOF'
[ERROR] 2024-06-01 08:11:55 upstream timed out (110: Connection timed out)
[ERROR] 2024-06-01 08:11:56 client: 10.0.0.5, server: api.example.com
EOF

# Create non-error log files
cat > /home/user/incident/logs/app.log << 'EOF'
INFO 2024-06-01 08:10:00 Server started
INFO 2024-06-01 08:12:30 Request received
EOF

cat > /home/user/incident/logs/db.log << 'EOF'
INFO 2024-06-01 08:10:05 DB pool initialized with 10 connections
EOF

cat > /home/user/incident/logs/system.info << 'EOF'
kernel: 5.15.0-91-generic
uptime: 14 days
EOF

# Set proper ownership
chown -R user:user /home/user
EOF
ENDSETUP

WORKDIR /home/user
