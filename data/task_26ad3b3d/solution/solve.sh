#!/bin/bash
set -e
cd /home/user

ls /home/user/audit/configs/
cat /home/user/audit/configs/webserver.ini
cat /home/user/audit/configs/database.ini
cat /home/user/audit/configs/mailrelay.ini
cat > /home/user/audit/report.txt << 'EOF'
=== COMPLIANCE AUDIT REPORT ===
Generated for: /home/user/audit/configs

--- database.ini ---
ssl_enabled: PASS
max_connections: PASS
log_level: PASS
auth_required: FAIL
timeout_seconds: FAIL
Status: NON-COMPLIANT

--- mailrelay.ini ---
ssl_enabled: PASS
max_connections: PASS
log_level: PASS
auth_required: PASS
timeout_seconds: PASS
Status: COMPLIANT

--- webserver.ini ---
ssl_enabled: PASS
max_connections: FAIL
log_level: FAIL
auth_required: PASS
timeout_seconds: PASS
Status: NON-COMPLIANT

=== SUMMARY ===
Total files checked: 3
Compliant: 1
Non-compliant: 2
Compliance rate: 33%

=== FAILED RULES ACROSS ALL FILES ===
max_connections: webserver.ini
log_level: webserver.ini
auth_required: database.ini
timeout_seconds: database.ini
EOF
cat /home/user/audit/report.txt
