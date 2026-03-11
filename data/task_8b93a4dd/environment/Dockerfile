FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the logs directory
mkdir -p /home/user/logs

# Create the service.log file with the expected content
cat > /home/user/logs/service.log << 'EOF'
[INFO] 2024-06-01 08:00:01 - Service started successfully
[INFO] 2024-06-01 08:00:05 - Loaded configuration from /etc/app/config.yaml
[WARN] 2024-06-01 08:01:12 - Disk usage at 78%, approaching threshold
[ERROR] 2024-06-01 08:02:34 - Failed to connect to database: connection refused
[INFO] 2024-06-01 08:02:40 - Retrying database connection (attempt 1)
[INFO] 2024-06-01 08:02:46 - Retrying database connection (attempt 2)
[ERROR] 2024-06-01 08:02:52 - Retry limit exceeded, giving up on database connection
[WARN] 2024-06-01 08:03:10 - Falling back to read-only mode
[INFO] 2024-06-01 08:05:00 - Health check passed (read-only)
[ERROR] 2024-06-01 08:10:15 - Null pointer exception in UserSessionHandler at line 42
[INFO] 2024-06-01 08:10:16 - Restarting UserSessionHandler
[INFO] 2024-06-01 08:15:00 - Health check passed
[WARN] 2024-06-01 08:20:33 - Memory usage at 91%, consider restarting
[ERROR] 2024-06-01 08:21:05 - Out of memory: failed to allocate 512MB for cache
[INFO] 2024-06-01 08:21:06 - Cache eviction triggered
[INFO] 2024-06-01 08:30:00 - Health check passed
[ERROR] 2024-06-01 08:45:22 - Unhandled exception in RequestRouter: timeout after 30s
[INFO] 2024-06-01 08:45:23 - RequestRouter reset
[WARN] 2024-06-01 09:00:01 - Config reload failed, using cached config
[ERROR] 2024-06-01 09:15:44 - Authentication service unreachable: no route to host
EOF

# Do NOT create error_count.txt or errors_only.log — the agent will create those

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
