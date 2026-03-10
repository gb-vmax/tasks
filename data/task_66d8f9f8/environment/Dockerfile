FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the metrics directory
mkdir -p /home/user/metrics

# Create the source file with the expected content
cat > /home/user/metrics/service_latency.txt << 'EOF'
service_name|environment|p50_ms|p95_ms|p99_ms
auth-service|production|12|45|120
payment-service|production|30|95|310
cart-service|staging|8|22|55
user-service|production|20|60|95
search-service|staging|15|80|210
notification-service|staging|5|18|88
billing-service|production|25|110|450
EOF

# Do NOT create high_latency.txt — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
