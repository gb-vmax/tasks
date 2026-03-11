FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the logs directory
mkdir -p /home/user/logs

# Create the nginx service log file with the expected content
cat > /home/user/logs/nginx-service.log << 'EOF'
2024-05-10T08:12:01 [INFO] Service started successfully
2024-05-10T08:13:45 [ERROR] Failed to bind to port 8080: address already in use
2024-05-10T08:14:02 [WARNING] Retrying connection to upstream
2024-05-10T08:14:10 [INFO] Upstream connection re-established
2024-05-10T08:15:33 [ERROR] Timeout reading from upstream: connection timed out
2024-05-10T08:16:01 [INFO] Health check passed
2024-05-10T08:17:45 [ERROR] Worker process 4821 exited with code 1
2024-05-10T08:18:00 [WARNING] High memory usage detected: 91%
2024-05-10T08:19:12 [INFO] Reloading configuration
2024-05-10T08:20:55 [ERROR] SSL certificate validation failed: certificate expired
EOF

# Do NOT create errors_only.log or error_summary.txt — those are output files the agent will create

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
