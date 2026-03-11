FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/incidents

cat > /home/user/incidents/raw_incidents.json << 'EOF'
[
  {"id":"INC-001","title":"Database connection pool exhausted","severity":"critical","status":"open","service":"postgres","opened_at":"2024-11-01T08:23:00Z"},
  {"id":"INC-002","title":"High memory usage on cache nodes","severity":"high","status":"resolved","service":"redis","opened_at":"2024-11-01T09:10:00Z"},
  {"id":"INC-003","title":"API gateway returning 503 errors","severity":"critical","status":"investigating","service":"api-gateway","opened_at":"2024-11-01T07:55:00Z"},
  {"id":"INC-004","title":"Disk usage above 90 percent","severity":"medium","status":"open","service":"filestore","opened_at":"2024-11-01T10:00:00Z"},
  {"id":"INC-005","title":"Payment service latency spike","severity":"high","status":"open","service":"payments","opened_at":"2024-11-01T09:45:00Z"},
  {"id":"INC-006","title":"SSL certificate expiring soon","severity":"low","status":"open","service":"nginx","opened_at":"2024-11-01T11:00:00Z"},
  {"id":"INC-007","title":"Auth service, token validation failing","severity":"critical","status":"open","service":"auth","opened_at":"2024-11-01T08:05:00Z"},
  {"id":"INC-008","title":"Search index out of sync","severity":"high","status":"investigating","service":"search","opened_at":"2024-11-01T08:50:00Z"},
  {"id":"INC-009","title":"Batch job failure in ETL pipeline","severity":"high","status":"resolved","service":"etl","opened_at":"2024-11-01T07:30:00Z"},
  {"id":"INC-010","title":"Object storage bucket unreachable","severity":"critical","status":"open","service":"storage","opened_at":"2024-11-01T09:00:00Z"}
]
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
