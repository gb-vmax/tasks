FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create legacy directory and script
mkdir -p /home/user/legacy

cat > /home/user/legacy/service_inventory.py << 'EOF'
services = [
    ("auth-service", "10.0.1.10", 8080, "active"),
    ("billing-service", "10.0.1.11", 8081, "inactive"),
    ("user-service", "10.0.1.12", 8082, "active"),
    ("notification-service", "10.0.1.13", 8083, "active"),
    ("report-service", "10.0.1.14", 8084, "inactive"),
    ("gateway-service", "10.0.1.15", 8085, "active"),
    ("cache-service", "10.0.1.16", 8086, "inactive"),
    ("search-service", "10.0.1.17", 8087, "active"),
]

for name, host, port, status in services:
    print(f"SERVICE={name} HOST={host} PORT={port} STATUS={status}")
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
