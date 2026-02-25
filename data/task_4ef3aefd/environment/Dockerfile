FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/logs

cat > /home/user/logs/service_status.log <<'EOF'
container_id: a1b2c3; name: api-service; image: micro/api:latest; status: running
container_id: d4e5f6; name: db-service; image: micro/db:5.6; status: stopped
container_id: g7h8i9; name: web-front; image: company/web:1.2; status: running
container_id: j1k2l3; name: cache; image: micro/cache:3.0; status: paused
container_id: m4n5o6; name: worker; image: micro/worker:latest; status: running
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
