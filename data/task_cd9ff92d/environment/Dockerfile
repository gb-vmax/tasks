FROM endless-deps-c84d384f2a25:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/monitoring

cat > /home/user/monitoring/uptime_report.json << 'EOF'
{
  "services": [
    {
      "name": "api-gateway",
      "sla_target_pct": 99.9,
      "checks": [
        {"timestamp": "2024-03-11T00:00:00Z", "status": "up", "response_time_ms": 142},
        {"timestamp": "2024-03-11T01:00:00Z", "status": "up", "response_time_ms": 138},
        {"timestamp": "2024-03-11T02:00:00Z", "status": "down", "response_time_ms": 0},
        {"timestamp": "2024-03-11T03:00:00Z", "status": "up", "response_time_ms": 155},
        {"timestamp": "2024-03-11T04:00:00Z", "status": "up", "response_time_ms": 149},
        {"timestamp": "2024-03-11T05:00:00Z", "status": "up", "response_time_ms": 161},
        {"timestamp": "2024-03-11T06:00:00Z", "status": "up", "response_time_ms": 133},
        {"timestamp": "2024-03-11T07:00:00Z", "status": "up", "response_time_ms": 144},
        {"timestamp": "2024-03-11T08:00:00Z", "status": "up", "response_time_ms": 158},
        {"timestamp": "2024-03-11T09:00:00Z", "status": "up", "response_time_ms": 147},
        {"timestamp": "2024-03-11T10:00:00Z", "status": "up", "response_time_ms": 139},
        {"timestamp": "2024-03-11T11:00:00Z", "status": "up", "response_time_ms": 162}
      ]
    },
    {
      "name": "auth-service",
      "sla_target_pct": 99.5,
      "checks": [
        {"timestamp": "2024-03-11T00:00:00Z", "status": "up", "response_time_ms": 85},
        {"timestamp": "2024-03-11T01:00:00Z", "status": "up", "response_time_ms": 91},
        {"timestamp": "2024-03-11T02:00:00Z", "status": "up", "response_time_ms": 88},
        {"timestamp": "2024-03-11T03:00:00Z", "status": "up", "response_time_ms": 79},
        {"timestamp": "2024-03-11T04:00:00Z", "status": "up", "response_time_ms": 93},
        {"timestamp": "2024-03-11T05:00:00Z", "status": "up", "response_time_ms": 87},
        {"timestamp": "2024-03-11T06:00:00Z", "status": "up", "response_time_ms": 82},
        {"timestamp": "2024-03-11T07:00:00Z", "status": "up", "response_time_ms": 90},
        {"timestamp": "2024-03-11T08:00:00Z", "status": "up", "response_time_ms": 84},
        {"timestamp": "2024-03-11T09:00:00Z", "status": "up", "response_time_ms": 92},
        {"timestamp": "2024-03-11T10:00:00Z", "status": "up", "response_time_ms": 88},
        {"timestamp": "2024-03-11T11:00:00Z", "status": "up", "response_time_ms": 86}
      ]
    },
    {
      "name": "payments-api",
      "sla_target_pct": 99.95,
      "checks": [
        {"timestamp": "2024-03-11T00:00:00Z", "status": "up", "response_time_ms": 310},
        {"timestamp": "2024-03-11T01:00:00Z", "status": "down", "response_time_ms": 0},
        {"timestamp": "2024-03-11T02:00:00Z", "status": "down", "response_time_ms": 0},
        {"timestamp": "2024-03-11T03:00:00Z", "status": "up", "response_time_ms": 298},
        {"timestamp": "2024-03-11T04:00:00Z", "status": "up", "response_time_ms": 325},
        {"timestamp": "2024-03-11T05:00:00Z", "status": "down", "response_time_ms": 0},
        {"timestamp": "2024-03-11T06:00:00Z", "status": "up", "response_time_ms": 301},
        {"timestamp": "2024-03-11T07:00:00Z", "status": "up", "response_time_ms": 315},
        {"timestamp": "2024-03-11T08:00:00Z", "status": "up", "response_time_ms": 308},
        {"timestamp": "2024-03-11T09:00:00Z", "status": "up", "response_time_ms": 322},
        {"timestamp": "2024-03-11T10:00:00Z", "status": "up", "response_time_ms": 295},
        {"timestamp": "2024-03-11T11:00:00Z", "status": "up", "response_time_ms": 317}
      ]
    },
    {
      "name": "user-service",
      "sla_target_pct": 99.0,
      "checks": [
        {"timestamp": "2024-03-11T00:00:00Z", "status": "up", "response_time_ms": 210},
        {"timestamp": "2024-03-11T01:00:00Z", "status": "up", "response_time_ms": 205},
        {"timestamp": "2024-03-11T02:00:00Z", "status": "up", "response_time_ms": 198},
        {"timestamp": "2024-03-11T03:00:00Z", "status": "up", "response_time_ms": 222},
        {"timestamp": "2024-03-11T04:00:00Z", "status": "up", "response_time_ms": 215},
        {"timestamp": "2024-03-11T05:00:00Z", "status": "up", "response_time_ms": 208},
        {"timestamp": "2024-03-11T06:00:00Z", "status": "up", "response_time_ms": 201},
        {"timestamp": "2024-03-11T07:00:00Z", "status": "up", "response_time_ms": 218},
        {"timestamp": "2024-03-11T08:00:00Z", "status": "up", "response_time_ms": 225},
        {"timestamp": "2024-03-11T09:00:00Z", "status": "up", "response_time_ms": 212},
        {"timestamp": "2024-03-11T10:00:00Z", "status": "up", "response_time_ms": 207},
        {"timestamp": "2024-03-11T11:00:00Z", "status": "up", "response_time_ms": 219}
      ]
    }
  ]
}
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
