#!/bin/bash
set -e
cd /home/user

ls /home/user/audit_logs/
mkdir -p /home/user/archive
tar -czf /home/user/archive/Q3_audit.tar.gz -C /home/user $(find audit_logs -maxdepth 1 -name "*.log" -type f 2>/dev/null | sort)
cd /home/user/archive && sha256sum Q3_audit.tar.gz > Q3_audit.tar.gz.sha256
echo "=== Archive contents ===" && tar -tzf /home/user/archive/Q3_audit.tar.gz && echo "" && echo "=== Checksum file ===" && cat /home/user/archive/Q3_audit.tar.gz.sha256 && echo "" && echo "=== Verification ===" && cd /home/user/archive && sha256sum -c Q3_audit.tar.gz.sha256
