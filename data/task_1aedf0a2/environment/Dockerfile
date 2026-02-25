FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/microservices/logs

cat > /home/user/microservices/logs/service-api.log <<EOF
2024-06-10 08:11:37 INFO Service started
2024-06-10 08:12:18 WARN Cache miss for user profile
2024-06-10 08:12:45 ERROR Failed to connect to Redis
2024-06-10 08:14:22 INFO User login: alice
2024-06-10 08:15:01 ERROR Service unavailable
2024-06-10 08:17:30 INFO Health check OK
2024-06-10 08:18:12 ERROR Payment gateway timeout
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
