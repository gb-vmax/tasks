FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/logs

cat > /home/user/logs/app.log << 'EOF'
2024-04-01T08:00:01Z INFO  Server started on port 8080
2024-04-01T08:00:45Z INFO  Connected to database
2024-04-01T08:01:12Z ERROR Failed to load config file: missing key 'timeout'
2024-04-01T08:01:30Z WARN  Retrying database connection (attempt 1)
2024-04-01T08:01:55Z INFO  Request received: GET /api/status
2024-04-01T08:02:10Z ERROR Null pointer exception in UserService.getById()
2024-04-01T08:02:11Z INFO  Request received: POST /api/login
2024-04-01T08:03:00Z INFO  Cache warmed up successfully
2024-04-01T08:03:45Z WARN  High memory usage detected: 82%
2024-04-01T08:04:01Z ERROR Disk write failed: /var/data/session_store
2024-04-01T08:04:02Z INFO  Fallback to in-memory store activated
2024-04-01T08:05:15Z INFO  Request received: GET /api/users
2024-04-01T08:05:45Z ERROR Connection timeout to upstream service: payments-svc
2024-04-01T08:06:00Z INFO  Scheduled job 'cleanup' started
2024-04-01T08:06:30Z INFO  Scheduled job 'cleanup' completed
2024-04-01T08:07:10Z WARN  Rate limit threshold approaching for client 10.0.0.5
2024-04-01T08:07:55Z ERROR Unhandled exception in request pipeline: NullReferenceException
2024-04-01T08:08:30Z INFO  Health check passed
2024-04-01T08:09:00Z ERROR Authentication service unavailable
2024-04-01T08:09:45Z INFO  Request received: DELETE /api/session/4892
2024-04-01T08:10:20Z WARN  Deprecated API endpoint called: /api/v1/users
2024-04-01T08:11:00Z INFO  Graceful shutdown initiated
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
