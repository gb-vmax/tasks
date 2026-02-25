FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/logs

cat > /home/user/logs/app.log <<'EOF'
ERROR Could not connect to database at 192.168.1.10:5432
INFO Started background job for data sync
WARN Low disk space on device /dev/sda1
User 10.20.30.40 accessed the admin console
ERROR Failed to bind to 0.0.0.0:8080 - port in use
INFO All background jobs completed
DEBUG Sent payload to 172.16.254.1 for user sync
ERROR Unexpected exception occurred
INFO Connection from 127.0.0.1 succeeded
ERROR Invalid input from user at 2001:0db8:85a3:0000:0000:8a2e:0370:7334
NOTICE Application shutdown initiated
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
