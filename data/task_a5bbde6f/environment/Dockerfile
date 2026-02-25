FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/obs-data

cat > /home/user/obs-data/service_health.csv <<EOF
service_name,status,response_time_ms,checked_at
api_gateway,success,134,2023-10-10T14:22:00Z
payment_service,fail,530,2023-10-10T14:23:00Z
api_gateway,fail,642,2023-10-10T14:24:00Z
user_service,success,212,2023-10-10T14:25:00Z
user_service,success,230,2023-10-10T14:26:00Z
api_gateway,success,140,2023-10-10T14:27:00Z
payment_service,success,510,2023-10-10T14:28:00Z
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
