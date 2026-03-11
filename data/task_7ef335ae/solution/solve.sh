#!/bin/bash
set -e
cd /home/user

cat /home/user/configs/service.yaml
cat /home/user/configs/app.toml
mkdir -p /home/user/diagnostics
cat > /home/user/diagnostics/report.txt << 'EOF'
=== DIAGNOSTIC REPORT ===

[SERVICE]
name: auth-service
version: 2.4.1
environment: production

[DATABASE]
host: db-primary.internal
port: 5432

[SERVER]
host: 0.0.0.0
port: 8080
timeout: 30

[LOGGING]
level: warn
file: /var/log/app/app.log
EOF
cat /home/user/diagnostics/report.txt
xxd /home/user/diagnostics/report.txt | tail -5
od -c /home/user/diagnostics/report.txt | tail -5
