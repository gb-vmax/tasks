FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/oncall

cat > /home/user/oncall/incidents.log << 'EOF'
2024-06-01T08:15:00|INC-0042|CRITICAL|auth-service|Token validation failure
2024-06-01T08:17:00|INC-0043|LOW|billing-service|Invoice render delay
2024-06-01T08:22:00|INC-0044|HIGH|api-gateway|Upstream connection timeout
2024-06-01T08:35:00|INC-0045|MEDIUM|cache-layer|Cache miss rate elevated
2024-06-01T08:41:00|INC-0046|CRITICAL|database|Replication Failure detected
2024-06-01T08:55:00|INC-0047|HIGH|auth-service|Session Timeout on login endpoint
2024-06-01T09:03:00|INC-0048|LOW|notifier|Email queue backed up
2024-06-01T09:10:00|INC-0049|CRITICAL|payment-service|Payment processing failure
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
