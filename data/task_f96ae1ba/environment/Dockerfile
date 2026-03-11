FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the logs directory
mkdir -p /home/user/logs

# Create the uptime monitor log file with the expected content
cat > /home/user/logs/uptime_monitor.log << 'EOF'
[2024-06-10T08:00:01Z] [INFO] host=api.example.com status=UP response_time_ms=98 check_id=chk_001
[2024-06-10T08:00:15Z] [ERROR] host=db.internal status=DOWN response_time_ms=5003 check_id=chk_002
[2024-06-10T08:00:30Z] [INFO] host=cache.internal status=UP response_time_ms=210 check_id=chk_003
[2024-06-10T08:01:00Z] [ERROR] host=payments.example.com status=TIMEOUT response_time_ms=30001 check_id=chk_004
[2024-06-10T08:01:15Z] [INFO] host=api.example.com status=UP response_time_ms=105 check_id=chk_005
[2024-06-10T08:01:30Z] [ERROR] host=auth.internal status=DOWN response_time_ms=9999 check_id=chk_006
[2024-06-10T08:02:00Z] [INFO] host=cache.internal status=UP response_time_ms=188 check_id=chk_007
[2024-06-10T08:02:15Z] [ERROR] host=db.internal status=TIMEOUT response_time_ms=30001 check_id=chk_008
[2024-06-10T08:02:45Z] [INFO] host=payments.example.com status=UP response_time_ms=312 check_id=chk_009
[2024-06-10T08:03:00Z] [INFO] host=api.example.com status=UP response_time_ms=99 check_id=chk_010
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
