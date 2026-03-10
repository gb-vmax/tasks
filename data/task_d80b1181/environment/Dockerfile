FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/observability

cat > /home/user/observability/dashboards.json << 'EOF'
{
  "dashboards": [
    {"name": "cpu-usage", "status": "ok", "threshold": 85},
    {"name": "memory-pressure", "status": "error", "threshold": 70},
    {"name": "disk-io", "status": "ok"},
    {"name": "network-latency", "status": "error"},
    {"name": "request-rate", "status": "ok", "threshold": 500},
    {"name": "error-budget", "status": "error", "threshold": 10},
    {"name": "pod-restarts", "status": "ok"},
    {"name": "db-connections", "status": "ok", "threshold": 100}
  ]
}
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
