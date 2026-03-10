#!/bin/bash
set -e
cd /home/user

ls -la /home/user/monitoring/ && ls -la /home/user/monitoring/config/
chmod 0750 /home/user/monitoring/healthcheck.sh && chmod 0600 /home/user/monitoring/config/api_credentials.conf
cat > /home/user/monitoring/audit_report.txt << 'EOF'
=== SECURITY AUDIT REPORT ===
Date: 2024-01-15
Auditor: sre-bot

VULNERABILITIES FIXED:

[1] healthcheck.sh
    Previous permissions: 0777
    Fixed permissions: 0750
    Risk: World-writable script executed by cron - arbitrary code injection

[2] api_credentials.conf
    Previous permissions: 0644
    Fixed permissions: 0600
    Risk: World-readable credentials file - API key exposure

STATUS: RESOLVED
EOF
chmod 0640 /home/user/monitoring/audit_report.txt
stat /home/user/monitoring/healthcheck.sh /home/user/monitoring/config/api_credentials.conf /home/user/monitoring/audit_report.txt && echo "---" && cat /home/user/monitoring/audit_report.txt
