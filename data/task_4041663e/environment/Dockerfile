FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/logs

cat > /home/user/logs/testapp.log <<EOF
2024-04-11 10:12:01 INFO Starting application
2024-04-11 10:12:03 WARNING Deprecated configuration detected
2024-04-11 10:12:07 ERROR Failed to connect to database
2024-04-11 10:12:09 INFO Database retry attempt 1
2024-04-11 10:12:11 WARNING Low disk space
2024-04-11 10:12:13 ERROR Could not locate config file
2024-04-11 10:12:16 INFO Application shutdown complete
EOF

cat > /home/user/logs/filtered_report.txt <<EOF
2024-04-11 10:12:03 WARNING Deprecated configuration detected
2024-04-11 10:12:07 ERROR Failed to connect to database
2024-04-11 10:12:11 WARNING Low disk space
2024-04-11 10:12:13 ERROR Could not locate config file
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
