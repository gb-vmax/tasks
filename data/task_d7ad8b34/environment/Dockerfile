FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/appdata
mkdir -p /home/user/diagnostics

cat > /home/user/appdata/app.log <<'EOF'
2024-06-09 17:45:22 [INFO] Pre-start checks completed.
2024-06-10 08:00:00 [ERROR] Startup failed: missing config file.
2024-06-10 08:00:05 [INFO] Attempting automated repair.
2024-06-11 13:20:48 [WARN] Deprecated API usage detected.
2024-06-11 14:21:00 [DEBUG] Heartbeat received.
2024-06-13 20:18:15 [ERROR] Database unavailable.
2024-06-14 03:02:35 [WARN] High memory usage warning.
2024-06-16 22:59:59 [ERROR] Critical failure in processing module.
2024-06-17 00:10:01 [WARN] Log rotation close failure.
EOF

# Ensure correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
