FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/logs

cat > /home/user/logs/nginx_app.log <<'EOF'
2024-06-10 10:00:01 [INFO] nginx service starting.
2024-06-10 10:00:03 [ERROR] nginx failed to start: Address already in use.
2024-06-10 10:00:10 [WARN] retrying nginx start.
2024-06-10 10:00:12 [ERROR] nginx configuration file /etc/nginx/nginx.conf not found.
2024-06-10 10:01:00 [INFO] nginx service stopped.
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
